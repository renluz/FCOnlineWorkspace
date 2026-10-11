import sys
import argparse
from pathlib import Path
from .verifier import TacticVerifier

# Ensure UTF-8 output on Windows terminal
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(
        description="FCOnlineWorkspace Tactic Verifier (3-Tier Quality Gate)"
    )
    parser.add_argument("tactic_file", help="Đường dẫn file JSON chiến thuật cần kiểm định")
    parser.add_argument("--squad", help="Đường dẫn file 02_CURRENT_SQUAD.json (tự động tìm nếu bỏ trống)")
    parser.add_argument("--configs", help="Đường dẫn file 04_PLAYER_CONFIGS.json (tự động tìm nếu bỏ trống)")
    parser.add_argument("--baseline", help="Đường dẫn file baseline để kiểm tra Single Variable A/B test")
    parser.add_argument("--allow-multi", action="store_true", help="Bỏ qua cờ kiểm tra kỷ luật đơn biến")
    parser.add_argument("--json", action="store_true", help="Xuất kết quả dưới dạng JSON thô")

    args = parser.parse_args()

    verifier = TacticVerifier(allow_multi_variables=args.allow_multi)
    result = verifier.verify_file(
        tactic_path=args.tactic_file,
        squad_path=args.squad,
        configs_path=args.configs,
        baseline_path=args.baseline
    )

    if args.json:
        print(result.model_dump_json(indent=2))
        sys.exit(0 if result.status != "FAIL" else 1)

    print("\n" + "=" * 70)
    print("🛡️  KẾT QUẢ KIỂM ĐỊNH CHIẾN THUẬT (TACTIC VERIFIER V2)")
    print("=" * 70)
    print(f"📁 File kiểm tra : {result.verified_file}")
    print(f"⏱️  Thời gian    : {result.timestamp}")
    print(f"📊 Trạng thái    : {result.status}")
    print(f"📈 Thống kê      : Đạt {result.summary.passed}/{result.summary.total_rules_checked} luật | Lỗi: {result.summary.errors_count} | Cảnh báo: {result.summary.warnings_count}")
    print("-" * 70)

    if result.errors:
        print("\n❌ DANH SÁCH LỖI (ERRORS):")
        for i, err in enumerate(result.errors, 1):
            print(f"  {i}. [{err.rule_id}][{err.severity}] Vị trí: {err.path}")
            print(f"     ➔ {err.message}")

    if result.warnings:
        print("\n⚠️  DANH SÁCH CẢNH BÁO (WARNINGS):")
        for i, warn in enumerate(result.warnings, 1):
            print(f"  {i}. [{warn.rule_id}][{warn.severity}] Vị trí: {warn.path}")
            print(f"     ➔ {warn.message}")

    if not result.errors and not result.warnings:
        print("\n✨ XUẤT SẮC! Cấu hình chiến thuật hoàn toàn hợp lệ, không có lỗi hay cảnh báo.")

    print("=" * 70 + "\n")

    sys.exit(0 if result.status != "FAIL" else 1)


if __name__ == "__main__":
    main()
