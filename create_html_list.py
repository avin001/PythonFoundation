def html_list(input_list):
    html_string = '<ul>\n'
    for item in input_list:
        html_string += '<li>{}</li>\n'.format(item)
    html_string += '</ul>'
    return html_string


print(html_list(['first string', 'second string']))
