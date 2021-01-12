import numpy as np
import scipy.stats as stats

def p_value_invariant_ab(data, group):
    '''
    based on binomial distribution, gets probability that a distribution of A/B group is outside of the corridor
    defined by the current distribution: "if n = ... and p = 0.5, what is the probability that X <= ...?"
    :param data:
    :param group:
    :return: p_value for
    '''
    # get number of trials and number of 'successes' (=participant assigned to specific group)
    n = data.sum()
    n_group = group.sum()

    # get standard dev for assumed 50/50 distribution
    p = 0.5
    std = np.sqrt(n*p*(1-p))

    # z-score for assumed 50/50 distribution and contituity correction
    x_mean = n*p
    x_i = n_group+0.5
    # account for the smaller group left of the mean...
    if x_i <= x_mean:
        z = (x_i - x_mean) / std
    # ...and the larger one right of the mean
    else:
        z = ((n-x_i) - x_mean) / std

    # p-value for participants assigned to each group as area under the curve
    # (calculation for area left of the mean *2 gets both areas under the curve)
    p_group = 2*stats.norm.cdf(z)

    return p_group

def p_value_eval_onetailed(group_con, group_exp, cond_con, cond_exp):
    # get number of trials, number of successes per group and and overall 'success' rate under null
    n_control = group_con.sum()
    n_exper = group_exp.sum()
    p_control = cond_con.sum() / n_control
    p_exper = cond_exp.sum() / n_exper
    p_null = (cond_con.sum() + cond_exp.sum()) / (n_control + n_exper)

    # null hypothesis: compute standard error, z-score, and p-value
    se = np.sqrt(p_null * (1-p_null) * (1/n_control + 1/n_exper))
    # calculate the differences in the evaluation metric between groups
    z = (p_exper - p_control) / se

    p_value = 1-stats.norm.cdf(z)

    return p_value