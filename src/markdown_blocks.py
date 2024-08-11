BLOCK_TYPE_PARAGRAPH = "paragraph"
BLOCK_TYPE_HEADING = "heading"
BLOCK_TYPE_CODE = "code"
BLOCK_TYPE_QUOTE = "quote"
BLOCK_TYPE_UNORDERED_LIST = "unordered_list"
BLOCK_TYPE_ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str):
    final_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block != "":
            stripped_block = block.strip()
            final_blocks.append(stripped_block)
    return final_blocks

def block_to_block_type(block: str):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return BLOCK_TYPE_HEADING

    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return BLOCK_TYPE_CODE

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BLOCK_TYPE_PARAGRAPH
        return BLOCK_TYPE_QUOTE

    if block.startswith("* "):
        for line in lines:
            if not block.startswith("* "):
                return BLOCK_TYPE_PARAGRAPH
        return BLOCK_TYPE_UNORDERED_LIST

    if block.startswith("- "):
        for line in lines:
            if not block.startswith("- "):
                return BLOCK_TYPE_PARAGRAPH
        return BLOCK_TYPE_UNORDERED_LIST

    if block.startswith("1. "):
        count = 1
        for line in lines:
            if not line.startswith(f"{count}. "):
                return BLOCK_TYPE_PARAGRAPH
            count+=1
        return BLOCK_TYPE_ORDERED_LIST

    return BLOCK_TYPE_PARAGRAPH