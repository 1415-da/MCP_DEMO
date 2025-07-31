from mcp.server.fastmcp import fastMCP

mcp=fastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """
    _summary_
    Add two numbers
    """
    return a+b


@mcp.tool()
def multiply(a:int,b:int)->int:
    """
    Multiply two numbers
    """
    return a*b


if __name__=="__main__":
    mcp.run(transport="stdio")