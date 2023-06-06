from aois2 import get_sknf, get_sdnf, convert_scdnf

function = "a + (b ∙ !c)"
func = "a+(b*!c)"
func_sknf = convert_scdnf(get_sknf(func))
func_sdnf = convert_scdnf(get_sdnf(func))
print("Function: ",func)


dict = ['a', 'b' , 'c']
dict_cursed = ['x', 'y' , 'z']
def remove_doubling_pdnf(expr):
    final_res = ""
    expr = expr.split('+')
    used_const = []
    for i in range(len(expr)):
        if expr[i] not in used_const:
            if expr[i] in dict or expr[i] in dict_cursed:
                used_const.append(expr[i])
            final_res += expr[i]+ '+'
    return final_res[:-1]

def remove_doubling_pcnf(expr):
    final_res = ""
    expr = expr.split('∙')
    used_const = []
    for i in range(len(expr)):
        if expr[i] not in used_const:
            if expr[i] in dict or expr[i] in dict_cursed:
                used_const.append(expr[i])
            final_res += expr[i]+ '∙'
    return final_res[:-1]

def eval_exp(exp):
    result = []
    for i in [[' False ', ' False ', ' False '], [' False ', ' False ', ' True '], [' False ', ' True ', ' True '],
              [' False ', ' True ', ' False '], [' True ', ' False ', ' False '], [' True ', ' False ', ' True '],
              [' True ', ' True ', ' False '], [' True ', ' True ', ' True '], ]:
        result.append((eval(exp.replace('a', i[0]).replace('b', i[1]).replace('c', i[2]).replace('∙', 'and').replace('+','or').
               replace('!', 'not '))))
    return result



def change_expr(expr):
    final_res = ""
    for i in range(len(expr)):
        if expr[i] == '(':
            final_res += '('
        if expr[i] == '+':
            final_res += '+'
        if expr[i] == '∙':
            final_res += '∙'
        if expr[i] == ')':
            final_res += ')'
        if expr[i] == '!':
            if expr[i+1] == 'a':
                final_res += 'x'
            if expr[i+1] == 'b':
                final_res += 'y'
            if expr[i+1] == 'c':
                final_res += 'z'
        if expr[i-1] != '!':
            if expr[i] == 'a':
                final_res += 'a'
            if expr[i] == 'b':
                final_res += 'b'
            if expr[i] == 'c':
                final_res += 'c'
    return final_res

def reverse_change_expr(expr):
    final_res = ""
    for i in range(len(expr)):
        if expr[i] == '+':
            final_res += '+'
        if expr[i] == '∙':
            final_res += '∙'
        if expr[i] == 'x':
            final_res += '!a'
        if expr[i] == 'y':
            final_res += '!b'
        if expr[i] == 'z':
            final_res += '!c'
        if expr[i] == 'a':
            final_res += 'a'
        if expr[i] == 'b':
            final_res += 'b'
        if expr[i] == 'c':
            final_res += 'c'
    return final_res

def calculate_method_expression_pcnf(pcnf, cnf):
    source_str = cnf
    cnf_source = cnf.split('∙')
    cnf = cnf.replace('+', '').split('∙')
    notneeded = ""
    pcnf = pcnf.split('∙')
    match = []
    number_of_simillar = [0]*len(pcnf)
    for i in range(len(cnf)):
        intersectionString = []
        for j in range(len(pcnf)):
            match_times = 0
            for k in range(len(cnf[i])):
                if pcnf[j].count(cnf[i][k]):
                    match_times += 1
            if match_times == len(cnf[i]):
                intersectionString.append(j)
                number_of_simillar[j] += 1
        match.append(intersectionString)
    for i in range(len(match)):
        match_times = 0
        for k in range(len(match[i])):
            if number_of_simillar[match[i][k]] >= 2:
                match_times += 1
            if match_times == len(match[i]):
                notneeded += (cnf_source[i])
    return match, reverse_change_expr(source_str.replace(notneeded, "").replace('++', '+').replace('∙∙', '∙'))

def calculate_method_expression_pdnf(pdnf, dnf):
    source_str = dnf
    dnf_source = dnf.split('+')
    dnf = dnf.replace('∙', '').split('+')
    notneeded = ""
    pdnf = pdnf.split('+')
    match = []
    number_of_simillar = [0]*len(pdnf)
    for i in range(len(dnf)):
        intersectionString = []
        for j in range(len(pdnf)):
            match_times = 0
            for k in range(len(dnf[i])):
                if pdnf[j].count(dnf[i][k]):
                    match_times += 1
            if match_times == len(dnf[i]):
                intersectionString.append(j)
                number_of_simillar[j] += 1
        match.append(intersectionString)
    for i in range(len(match)):
        match_times = 0
        for k in range(len(match[i])):
            if number_of_simillar[match[i][k]] >= 2:
                match_times += 1
            if match_times == len(match[i]):
                notneeded += (dnf_source[i])
    return match, reverse_change_expr(source_str.replace(notneeded, "").replace('++', '+').replace('∙∙', '∙'))

def tabular_method_pcnf(pcnf, cnf, matches, min_cnf):
    print("Tabular_calculated_method pdnf: ")
    print(reverse_change_expr(pcnf))
    cnf = cnf.replace('+', '').split('∙')
    pcnf = pcnf.replace('+', '').split('∙')
    for i in range(len(cnf)):
        print(' ')
        for j in range(len(pcnf)):
            for k in range(len(matches[i])):
                print('X', end= " ") if matches[i][k] == j else print(' ', end= " ")
            print('  ', end="")
        print(reverse_change_expr(cnf[i]), end= " ")
    print('')
    print("Result: " + min_cnf)

def tabular_method_pdnf(pdnf, dnf, matches, min_dnf):
    print("Tabular_calculated_method pdnf: ")
    print(reverse_change_expr(pdnf))
    dnf = dnf.replace('∙', '').split('+')
    pdnf = pdnf.replace('∙', '').split('+')
    for i in range(len(dnf)):
        print(' ')
        for j in range(len(pdnf)):
            for k in range(len(matches[i])):
                print('X', end= " ") if matches[i][k] == j else print(' ', end= " ")
            print('  ', end="")
        print(reverse_change_expr(dnf[i]), end= " ")
    print('')
    print("Result: " + min_dnf)

def calculate_expression_cnf(expr):
    used_index = []
    final_res = ""
    clear_expr = expr.replace("(", "").replace(")", "")
    clear_expressions = clear_expr.split('∙')
    for i in range(len(clear_expressions)):
        for j in range(i+1, len(clear_expressions)):
            temp1 = clear_expressions[i].split('+')
            temp2 = clear_expressions[j].split('+')
            if temp1[0] == temp2[0]:
                if temp1[1] in dict and temp2[1] in dict_cursed and dict.index(temp1[1]) == dict_cursed.index(temp2[1]):
                    final_res += temp1[0] + '∙'
                    used_index.extend([i,j])
                if temp2[1] in dict and temp1[1] in dict_cursed and dict.index(temp2[1]) == dict_cursed.index(temp1[1]):
                    final_res += temp2[0] + '∙'
                    used_index.extend([i,j])
            if temp1[1] == temp2[1]:
                if temp1[0] in dict and temp2[0] in dict_cursed and dict.index(temp1[0]) == dict_cursed.index(temp2[0]):
                    final_res += temp1[1] + '∙'
                    used_index.extend([i,j])
                if temp2[0] in dict and temp1[0] in dict_cursed and dict.index(temp2[0]) == dict_cursed.index(temp1[0]):
                    final_res += temp2[1] + '∙'
                    used_index.extend([i,j])
    for i in range(len(clear_expressions)):
        if i not in used_index:
            final_res += clear_expressions[i] + '∙'
    final_res = final_res[:-1]
    return final_res

def calculate_expression_dnf(expr):
    used_index = []
    final_res = ""
    clear_expr = expr.replace("(", "").replace(")", "")
    clear_expressions = clear_expr.split('+')
    for i in range(len(clear_expressions)):
        for j in range(i+1, len(clear_expressions)):
            temp1 = clear_expressions[i].split('∙')
            temp2 = clear_expressions[j].split('∙')
            if temp1[0] == temp2[0]:
                if temp1[1] in dict and temp2[1] in dict_cursed and dict.index(temp1[1]) == dict_cursed.index(temp2[1]):
                    final_res += temp1[0] + '+'
                    used_index.extend([i,j])
                if temp2[1] in dict and temp1[1] in dict_cursed and dict.index(temp2[1]) == dict_cursed.index(temp1[1]):
                    final_res += temp2[0] + '+'
                    used_index.extend([i,j])
            if temp1[1] == temp2[1]:
                if temp1[0] in dict and temp2[0] in dict_cursed and dict.index(temp1[0]) == dict_cursed.index(temp2[0]):
                    final_res += temp1[1] + '+'
                    used_index.extend([i,j])
                if temp2[0] in dict and temp1[0] in dict_cursed and dict.index(temp2[0]) == dict_cursed.index(temp1[0]):
                    final_res += temp2[1] + '+'
                    used_index.extend([i,j])
    for i in range(len(clear_expressions)):
        if i not in used_index:
            final_res += clear_expressions[i] + '+'
    final_res = final_res[:-1]
    return final_res

def carno(function):
    print("Tabular: ")
    row_first = []
    row_second = []
    row_first.append(function[0])
    row_first.append(function[1])
    row_first.append(function[2])
    row_first.append(function[3])
    row_second.append(function[4])
    row_second.append(function[5])
    row_second.append(function[7])
    row_second.append(function[6])
    carno = [row_first, row_second]
    return carno

def tabular_dnf(carno,dnf):
    print("a/bc | 00 | 01 | 11 | 10 |")
    for i in range(len(carno)):
        if i == 0:
            print(" 0 /", end=" ")
        else:
            print(" 1 /", end=" ")
        for j in range(len(carno[i])):
            print(carno[i][j], end=" ")
            if j != len(carno[i]):
                print("|", end=" ")
        print("")
    print("Result: ", dnf)

def tabular_knf(carno,knf):
    print("a/bc | 00 | 01 | 11 | 10 |")
    for i in range(len(carno)):
        if i == 0:
            print(" 0 /", end=" ")
        else:
            print(" 1 /", end=" ")
        for j in range(len(carno[i])):
            print(carno[i][j], end=" ")
            if j != len(carno[i]):
                print("|", end=" ")
        print("")
    print("Result: ", knf)

def gluing_method_pcnf_new(pcnf):
    itog = ""
    expressions = pcnf.split('∙')
    for i in range(len(expressions)):
        for j in range(i+1, len(expressions)):
            result_expression = ""
            temp1 = expressions[i].replace("(", "").replace(")", "")
            temp2 = expressions[j].replace("(", "").replace(")", "")
            variables_temp1 = temp1.split('+')
            variables_temp2 = temp2.split('+')
            count = 0
            for k in range(len(variables_temp1)):
                if variables_temp1[k] == variables_temp2[k]:
                    result_expression += variables_temp1[k] + "+"
                    count += 1
            if count == 2:
                result_expression = result_expression[:-1]
                result_expression = '(' + result_expression + ')'
                itog += result_expression + '∙'
    itog = itog[:-1]
    return itog

def gluing_method_pdnf_new(pdnf):
    itog = ""
    expressions = pdnf.split('+')
    for i in range(len(expressions)):
        for j in range(i+1, len(expressions)):
            result_expression = ""
            temp1 = expressions[i].replace("(", "").replace(")", "")
            temp2 = expressions[j].replace("(", "").replace(")", "")
            variables_temp1 = temp1.split('∙')
            variables_temp2 = temp2.split('∙')
            count = 0
            for k in range(len(variables_temp1)):
                if variables_temp1[k] == variables_temp2[k]:
                    result_expression += variables_temp1[k] + "∙"
                    count += 1
            if count == 2:
                result_expression = result_expression[:-1]
                result_expression = '(' + result_expression + ')'
                itog += result_expression + '+'
    itog = itog[:-1]
    return itog

def operations_pdnf(pdnf, function):
    print("PDNF: ", func_sdnf)
    glued_dnf = remove_doubling_pdnf(calculate_expression_dnf(change_expr(gluing_method_pdnf_new(pdnf))))
    matches, minimized_dnf = (calculate_method_expression_pdnf(change_expr(pdnf), glued_dnf))
    print("Minimized dnf: " + minimized_dnf)
    tabular_method_pdnf(change_expr(pdnf), glued_dnf, matches, minimized_dnf)
    function_values = eval_exp(function)
    tabular_dnf(carno(function_values),minimized_dnf)

def operations_pcnf(pcnf,function):
    print("PCNF: ", func_sknf)
    glued_cnf = remove_doubling_pcnf(calculate_expression_cnf(change_expr(gluing_method_pcnf_new(pcnf))))
    matches, minimized_cnf = (calculate_method_expression_pcnf(change_expr(pcnf), glued_cnf))
    print("Minimized_cnf: " + minimized_cnf)
    tabular_method_pcnf(change_expr(pcnf), glued_cnf, matches, minimized_cnf)
    function_values = eval_exp(function)
    tabular_knf(carno(function_values), minimized_cnf)

operations_pcnf(func_sknf, function)
operations_pdnf(func_sdnf, function)