import json

def parse_nb():
    with open('DL_dogbreedclassifier_latest.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    with open('parsed_nb.txt', 'w', encoding='utf-8') as out:
        for i, c in enumerate(nb.get('cells', [])):
            if c['cell_type'] == 'markdown':
                out.write(f"\n[MARKDOWN]\n")
                out.write(''.join(c.get('source', [])) + '\n')
            elif c['cell_type'] == 'code':
                source = ''.join(c.get('source', []))
                out.write(f"\n[CODE]\n{source[:100]}...\n")
                out.write("--- OUTPUT ---\n")
                for o in c.get('outputs', []):
                    if o.get('output_type') == 'stream':
                        text = ''.join(o.get('text', []))
                        lines = [l for l in text.split('\n') if 'inflating:' not in l and 'Streaming output truncated' not in l]
                        out.write('\n'.join(lines[:10]) + ('\n[...]\n' if len(lines) > 10 else '\n'))
                    else:
                        d = o.get('data', {})
                        if 'text/plain' in d:
                            out.write(''.join(d['text/plain']) + '\n')
                        if 'image/png' in d:
                            out.write("[Image Output]\n")

if __name__ == '__main__':
    parse_nb()
