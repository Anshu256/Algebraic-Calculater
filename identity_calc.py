factors = []
ftr_indx,term_indx = 0,0
while True:
    factors.append([])
    while True:
        factor_term = input(f"Enter the term {term_indx} of factor {ftr_indx}('E' to end factor): ")
        if factor_term == 'E':
            break
        factors[ftr_indx].append(factor_term)
        term_indx += 1
    if term_indx == 0:
        print("equation ended as last factor was 1")
        factors.pop()
        break
    term_indx = 0
    ftr_indx += 1

print(factors)

def make_identity(curr_term_of_prev_factor,ftr_idx):
    if ftr_idx == len(factors):
        return curr_term_of_prev_factor
    str_all_multiply = ""
    for term in factors[ftr_idx]:
        str_all_multiply += curr_term_of_prev_factor + ' . ' + make_identity(term,ftr_idx+1) + ' + '
    str_all_multiply = str_all_multiply[:-2] + ' '
    #if ftr_idx == len(factors)-1:
    return str_all_multiply

def get_terms(identity):
    identity += '+'
    terms = []
    temp_term = ''
    is_in_term = True
    for digit in identity:
        if digit == '+':
            is_in_term = False
            terms.append(temp_term)
            temp_term = ''
        else:
            is_in_term = True
        if is_in_term:
            temp_term += digit
    return terms

def simplify_multi(terms_list):
    simplified_terms = []
    for term in terms_list:
        temp_nums = []
        temp_vars = {}
        list_vars = []
        is_in_num = False
        for place in term:
            if place.isdigit():
                if is_in_num:
                    temp_nums[-1] *= 10
                    temp_nums[-1] += int(place)
                else:
                    temp_nums.append(int(place))
                    is_in_num = True
            elif place == '.':
                is_in_num = False

            elif place.isalpha() and place != ' ':
                #if temp_vars[place] != None:
                try:
                    temp_vars[place] += 1
                #else:
                except KeyError:
                    temp_vars[place] = 1
                    list_vars.append(place)
                is_in_num = False
            
        coeff = 1
        for i in temp_nums:
            coeff *= i
        var_block = ''
        for i in list_vars:
            var_block += i + '^' + str(temp_vars[i])
        simplified_terms.append(str(coeff) + var_block)
    return simplified_terms

def simplify_add(terms):
    var_blocks = {}
    for term in terms:
        const_coeff = 0
        varblock_not_started = True
        for place in term:
            if place.isdigit() and varblock_not_started:
                const_coeff = const_coeff * 10 + int(place)
            elif place.isalpha():
                varblock_not_started = False
                

            


iden = make_identity('1',0)
print(iden)
terms = get_terms(iden)
print(terms)
simpleIdentity = simplify_multi(terms)
print(simpleIdentity)

# input should be able to take powered variables
