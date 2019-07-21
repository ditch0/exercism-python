import re


def replace_headers(line):
    def replace(match):
        tag = 'h{}'.format(len(match['code']))
        return '<{0}>{1}</{0}>'.format(tag, match['content'])

    return re.sub(r'^(?P<code>#+) (?P<content>.*)', replace, line)


def replace_code_with_tag(line, code, tag):
    return re.sub(
        fr'{code}(.*){code}',
        fr'<{tag}>\1</{tag}>',
        line
    )


def add_p_tag(line):
    if re.match('<h|<ul|<p|<li', line):
        return line
    else:
        return '<p>' + line + '</p>'


def parse_markdown(markdown):
    lines = markdown.split('\n')
    html = ''
    in_list = False
    for line in lines:
        line = replace_headers(line)
        line = replace_code_with_tag(line, '__', 'strong')
        line = replace_code_with_tag(line, '_', 'em')

        match = re.match(r'\* (?P<list_item>.*)', line)
        if match:
            line = '<li>' + match['list_item'] + '</li>'
            if not in_list:
                in_list = True
                line = '<ul>' + line
        else:
            line = add_p_tag(line)
            if in_list:
                line = '</ul>' + line
                in_list = False

        html += line
    if in_list:
        html += '</ul>'
    return html
