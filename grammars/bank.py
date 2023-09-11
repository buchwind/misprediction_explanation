import string
from fuzzingbook.Grammars import srange, Grammar

#bank Grammar(after normalization and multiplication to remove negative and float values)
BANK: Grammar = {
    "<start>": ["<age> <contact> <month> <day_of_week> <duration> <campaign> <pdays> <previous> <emp_var_rate> <cons_price_idx> <cons_conf_idx> <euribor3m> <job_admin> <job_blue_collar> <job_entrepreneur> <job_housemaid> <job_management> <job_retired> <job_self_employed> <job_services> <job_student> <job_technician> <job_unemployed> <job_unknown> <marital_divorced> <marital_married> <marital_single> <education_basic_4y> <education_basic_6y> <education_basic_9y> <education_high_school> <education_illiterate> <education_professional_course> <education_university_degree> <education_unknown> <default_no> <default_unknown> <default_yes> <housing_no> <housing_unknown> <housing_yes> <loan_no> <loan_unknown> <loan_yes> <poutcome_failure> <poutcome_nonexistent> <poutcome_success> <employee_1> <employee_2> <employee_3> <employee_4> <employee_5> <employee_6> <employee_7> <employee_8> <employee_9> <employee_10>"],
    "<age>": ["0", "<onenine><maybe_digits>"],
    "<contact>": ["0", "<onenine><maybe_digits>"],
    "<month>": ["0", "<onenine><maybe_digits>"],
    "<day_of_week>": ["0", "<onenine><maybe_digits>"],
    "<duration>": ["0", "<onenine><maybe_digits>"],
    "<campaign>": ["0", "<onenine><maybe_digits>"],
    "<pdays>": ["0", "<onenine><maybe_digits>"],
    "<previous>": ["0", "<onenine><maybe_digits>"],
    "<emp_var_rate>": ["0", "<onenine><maybe_digits>"],
    "<cons_price_idx>": ["0", "<onenine><maybe_digits>"],
    "<cons_conf_idx>": ["0", "<onenine><maybe_digits>"],
    "<euribor3m>": ["0", "<onenine><maybe_digits>"],
    "<job_admin>": ["0", "<onenine><maybe_digits>"],
    "<job_blue_collar>": ["0", "<onenine><maybe_digits>"],
    "<job_entrepreneur>": ["0", "<onenine><maybe_digits>"],
    "<job_housemaid>": ["0", "<onenine><maybe_digits>"],
    "<job_management>": ["0", "<onenine><maybe_digits>"],
    "<job_retired>": ["0", "<onenine><maybe_digits>"],
    "<job_self_employed>": ["0", "<onenine><maybe_digits>"],
    "<job_services>": ["0", "<onenine><maybe_digits>"],
    "<job_student>": ["0", "<onenine><maybe_digits>"],
    "<job_technician>": ["0", "<onenine><maybe_digits>"],
    "<job_unemployed>": ["0", "<onenine><maybe_digits>"],
    "<job_unknown>": ["0", "<onenine><maybe_digits>"],
    "<marital_divorced>": ["0", "<onenine><maybe_digits>"],
    "<marital_married>": ["0", "<onenine><maybe_digits>"],
    "<marital_single>": ["0", "<onenine><maybe_digits>"],
    "<education_basic_4y>": ["0", "<onenine><maybe_digits>"],
    "<education_basic_6y>": ["0", "<onenine><maybe_digits>"],
    "<education_basic_9y>": ["0", "<onenine><maybe_digits>"],
    "<education_high_school>": ["0", "<onenine><maybe_digits>"],
    "<education_illiterate>": ["0", "<onenine><maybe_digits>"],
    "<education_professional_course>": ["0", "<onenine><maybe_digits>"],
    "<education_university_degree>": ["0", "<onenine><maybe_digits>"],
    "<education_unknown>": ["0", "<onenine><maybe_digits>"],
    "<default_no>": ["0", "<onenine><maybe_digits>"],
    "<default_unknown>": ["0", "<onenine><maybe_digits>"],
    "<default_yes>": ["0", "<onenine><maybe_digits>"],
    "<housing_no>": ["0", "<onenine><maybe_digits>"],
    "<housing_unknown>": ["0", "<onenine><maybe_digits>"],
    "<housing_yes>": ["0", "<onenine><maybe_digits>"],
    "<loan_no>": ["0", "<onenine><maybe_digits>"],
    "<loan_unknown>": ["0", "<onenine><maybe_digits>"],
    "<loan_yes>": ["0", "<onenine><maybe_digits>"],
    "<poutcome_failure>": ["0", "<onenine><maybe_digits>"],
    "<poutcome_nonexistent>": ["0", "<onenine><maybe_digits>"],
    "<poutcome_success>": ["0", "<onenine><maybe_digits>"],
    "<employee_1>": ["0", "<onenine><maybe_digits>"],
    "<employee_2>": ["0", "<onenine><maybe_digits>"],
    "<employee_3>": ["0", "<onenine><maybe_digits>"],
    "<employee_4>": ["0", "<onenine><maybe_digits>"],
    "<employee_5>": ["0", "<onenine><maybe_digits>"],
    "<employee_6>": ["0", "<onenine><maybe_digits>"],
    "<employee_7>": ["0", "<onenine><maybe_digits>"],
    "<employee_8>": ["0", "<onenine><maybe_digits>"],
    "<employee_9>": ["0", "<onenine><maybe_digits>"],
    "<employee_10>": ["0", "<onenine><maybe_digits>"],
    "<onenine>": srange("123456789"),
    "<maybe_digits>": ["", "<digits>"],
    "<digits>": ["<digit>", "<digit><digits>"],
    "<digit>": list(string.digits)
}
