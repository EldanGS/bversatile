from test_framework import generic_test


def find_salary_cap(target_payroll, current_salaries):
    current_salaries.sort()
    n = len(current_salaries)
    unadjusted_salary_sum = 0.0

    for i, salary in enumerate(current_salaries):
        adjusted_people = n - i
        adjusted_salary_sum = salary * adjusted_people

        if unadjusted_salary_sum + adjusted_salary_sum >= target_payroll:
            return (target_payroll - unadjusted_salary_sum) / adjusted_people

        unadjusted_salary_sum += salary

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("13-12-find_salary_threshold.py",
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
