import { pathToFileURL } from "node:url";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { loadConfig, type AppConfig } from "./config.js";
import { NexonClient } from "./nexon/client.js";
import { FcOnlineError } from "./nexon/errors.js";
import { NexonMetadataService } from "./nexon/metadata.js";
import { FcOnlineService } from "./service.js";
import { registerCompositeTools } from "./tools/composite.js";
import { registerRawTools } from "./tools/raw.js";

export function createServer(service: FcOnlineService) {
  const server = new McpServer({
    name: "fconline-mcp",
    version: "0.1.0"
  });

  registerRawTools(service, server);
  registerCompositeTools(service, server);

  return server;
}

export function createService(config: AppConfig) {
  const client = new NexonClient(config);
  const metadata = new NexonMetadataService(client, config);
  return new FcOnlineService(client, metadata, config);
}

async function main() {
  const config = loadConfig();
  const service = createService(config);
  const server = createServer(service);
  const transport = new StdioServerTransport();

  await server.connect(transport);
  console.error("fconline-mcp server is running on stdio");
}

const isMain = process.argv[1] !== undefined && import.meta.url === pathToFileURL(process.argv[1]).href;

if (isMain) {
  main().catch((error: unknown) => {
    const normalized = error instanceof FcOnlineError ? error : new FcOnlineError("UPSTREAM_ERROR", "서버 시작에 실패했습니다.", { cause: error });
    console.error(JSON.stringify(normalized.toJSON()));
    process.exit(1);
  });
}