def markdown_to_blocks(markdown: str):
    final_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block != "":
            stripped_block = block.strip()
            final_blocks.append(stripped_block)
    print(final_blocks)
    return final_blocks