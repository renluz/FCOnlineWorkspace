import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import * as z from "zod/v4";
import { createToolErrorPayload } from "../nexon/errors.js";

export const genericObjectOutputSchema = z.object({}).passthrough();
export const matchTypeInputSchema = z.union([z.string(), z.number()]);
export const lookupInputSchema = z.union([z.string(), z.number()]);
export const positiveIntegerSchema = z.number().int().min(0);

export function registerJsonTool<TInput extends z.ZodTypeAny>(options: {
  server: McpServer;
  name: string;
  description: string;
  inputSchema: TInput;
  handler: (args: z.infer<TInput>) => Promise<Record<string, unknown>>;
}) {
  (options.server.registerTool as any)(
    options.name,
    {
      description: options.description,
      inputSchema: options.inputSchema,
      outputSchema: genericObjectOutputSchema,
      annotations: {
        readOnlyHint: true,
        idempotentHint: true,
        openWorldHint: true
      }
    },
    async (args: z.infer<TInput>) => {
      try {
        const result = await options.handler(args);
        return {
          content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
          structuredContent: result
        };
      } catch (error) {
        const payload = createToolErrorPayload(error);
        return {
          isError: true,
          content: [{ type: "text", text: JSON.stringify(payload, null, 2) }],
          structuredContent: payload
        };
      }
    }
  );
}