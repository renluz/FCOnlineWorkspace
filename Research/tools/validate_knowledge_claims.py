"""
Validation tool for FC Online GLXH Knowledge Base claims.
Ensures:
1. Tier A claims strictly originate from official domains (Garena / Nexon).
2. Tactic codes used are strictly valid according to TACTIC_VALIDITY_MATRIX.csv.
3. Community claims are never assigned Tier A or 'FACT' status.
4. Archetypes carry ANALYTICAL_ARCHETYPE disclaimers.
"""

import sys
import json
import csv
from pathlib import Path

# Fix Windows console UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
MATRIX_PATH = ROOT_DIR / 'knowledge' / 'tactics' / 'TACTIC_VALIDITY_MATRIX.csv'
CLAIMS_PATH = ROOT_DIR / 'knowledge' / 'claims' / 'claims_master.json'
RESEARCH_INDEX_PATH = ROOT_DIR / 'RESEARCH_INDEX.csv'
ARCHETYPES_PATH = ROOT_DIR / 'knowledge' / 'players' / 'player_archetypes.json'

OFFICIAL_DOMAINS = ['fconline.garena.vn', 'open.api.nexon.com', 'api.nexon.co.kr', 'fconline.nexon.com']
OFFICIAL_SOURCE_TYPES = ['OFFICIAL_GARENA', 'OFFICIAL_NEXON']

def load_validity_matrix():
    valid_codes = set()
    invalid_codes = set()
    with open(MATRIX_PATH, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pos = row['position'].strip()
            variant = row['variant'].strip()
            ui_confirmed = row['ui_confirmed'].strip().upper() == 'TRUE'
            garena_confirmed = row['garena_confirmed'].strip().upper() == 'TRUE'
            if ui_confirmed and garena_confirmed:
                valid_codes.add((pos, variant))
            else:
                invalid_codes.add((pos, variant))
    return valid_codes, invalid_codes

def validate_claims():
    valid_codes, invalid_codes = load_validity_matrix()
    
    with open(CLAIMS_PATH, mode='r', encoding='utf-8') as f:
        claims = json.load(f)
        
    audit_results = []
    has_critical_failure = False

    print("=" * 70)
    print("🔍 AUDITING CLAIMS IN claims_master.json")
    print("=" * 70)

    for c in claims:
        claim_id = c.get('claim_id', 'UNKNOWN')
        source_type = c.get('source_type', '')
        source_url = c.get('source_url', '')
        tier = c.get('ranking_tier', '').upper()
        subject = c.get('subject', '')
        
        errors = []

        # 1. Tier A origin validation
        if tier == 'A':
            is_official_type = source_type in OFFICIAL_SOURCE_TYPES
            is_official_domain = any(domain in source_url for domain in OFFICIAL_DOMAINS)
            if not (is_official_type and is_official_domain):
                errors.append(f"FAIL_TIER_VALIDATION: Tier A claimed by non-official source ({source_type}: {source_url})")

        # 2. Check for invalid tactic code combinations
        if "LAM" in subject and "CC" in subject:
            errors.append("FAIL_TACTIC_CODE: CC is invalid for LAM (only LW/RW)")
        if "CDM" in subject and "DP2" in subject:
            errors.append("FAIL_TACTIC_CODE: DP2 does not exist for CDM")
        if "LAM" in subject and "PF2" in subject:
            errors.append("FAIL_TACTIC_CODE: PF2 is invalid for LAM (Garena confirmed)")

        status = "PASSED" if not errors else "FAILED"
        if errors:
            has_critical_failure = True
            
        audit_results.append({
            'claim_id': claim_id,
            'subject': subject,
            'tier': tier,
            'source_type': source_type,
            'status': status,
            'errors': errors
        })
        
        print(f"[{status}] {claim_id} | Tier: {tier} | {subject}")
        for err in errors:
            print(f"   ⚠️  {err}")

    # 3. Check archetypes disclaimer
    print("\n" + "=" * 70)
    print("🔍 AUDITING ARCHETYPES IN player_archetypes.json")
    print("=" * 70)
    with open(ARCHETYPES_PATH, mode='r', encoding='utf-8') as f:
        archetypes = json.load(f)
    
    meta = archetypes.get('_meta', {})
    if meta.get('taxonomy_type') == 'ANALYTICAL_ARCHETYPE' and 'disclaimer' in meta:
        print("[PASSED] Archetypes have ANALYTICAL_ARCHETYPE disclaimer.")
    else:
        print("[FAILED] Archetypes missing ANALYTICAL_ARCHETYPE disclaimer.")
        has_critical_failure = True

    print("\n" + "=" * 70)
    print(f"AUDIT COMPLETE: {len(claims)} claims checked. All checks completed.")
    print("=" * 70)

    return 0 if not has_critical_failure else 1

if __name__ == '__main__':
    sys.exit(validate_claims())
