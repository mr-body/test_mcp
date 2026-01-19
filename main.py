from mcp.server.fastmcp import FastMCP, Context, Icon
from pydantic import Field
import asyncio

mcp = FastMCP(
    "Test Server",
    icons=[
        Icon(
            src="vercel.svg",
            mimeType="image/svg+xml",
            sizes=["173x150"]
        )
    ],
    stateless_http=True,
    json_response=True,
)

@mcp.tool()
async def add(
    a: int = Field(description="First number to add"),
    b: int = Field(description="Second number to add"),
    ctx: Context = None
):
    """Add two numbers"""
    if ctx:
        await ctx.report_progress(10, 100)
        await ctx.info(f"Adding {a} and {b} ...")
        await ctx.report_progress(20, 100)
        await ctx.debug("Performing addition operation")

    await asyncio.sleep(1)

    if ctx:
        await ctx.debug("Addition in progress...")

    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"

@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    return f"Write a {style} greeting for someone named {name}."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
