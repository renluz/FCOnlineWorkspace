export type FcOnlineErrorCode =
  | "CONFIG_ERROR"
  | "VALIDATION_ERROR"
  | "UPSTREAM_ERROR"
  | "RATE_LIMITED"
  | "NOT_FOUND"
  | "NO_MATCHES"
  | "IMAGE_NOT_FOUND"
  | "TRADE_SCOPE_RESTRICTION";

export class FcOnlineError extends Error {
  readonly code: FcOnlineErrorCode;
  readonly status: number | undefined;
  readonly details: unknown;
  readonly retryAfterSeconds: number | undefined;

  constructor(
    code: FcOnlineErrorCode,
    message: string,
    options: {
      status?: number;
      details?: unknown;
      retryAfterSeconds?: number;
      cause?: unknown;
    } = {}
  ) {
    super(message, { cause: options.cause });
    this.name = "FcOnlineError";
    this.code = code;
    this.status = options.status;
    this.details = options.details;
    this.retryAfterSeconds = options.retryAfterSeconds;
  }

  toJSON() {
    return {
      code: this.code,
      message: this.message,
      status: this.status,
      retryAfterSeconds: this.retryAfterSeconds,
      details: this.details
    };
  }
}

export function toFcOnlineError(error: unknown): FcOnlineError {
  if (error instanceof FcOnlineError) {
    return error;
  }

  if (error instanceof Error) {
    return new FcOnlineError("UPSTREAM_ERROR", error.message, {
      cause: error
    });
  }

  return new FcOnlineError("UPSTREAM_ERROR", "알 수 없는 오류가 발생했습니다.", {
    details: error
  });
}

export function createToolErrorPayload(error: unknown) {
  const normalized = toFcOnlineError(error);

  return {
    ok: false,
    error: normalized.toJSON()
  };
}