#!/usr/bin/env python
# coding: utf-8

# # Domain driven models
# 
# Focus on business logic
# 
# Example Architecture
# 
# - Business
# - Person 
# - Evaluation
#     - Batch
#     - Rule

# In[10]:


from dataclasses import dataclass


# Let us see some of the benefits of using dataclasses to create our rules. Rule is a value object and what it means is that if we change one of its constituting parts the object comparison is different. 
# 
# Let's see in practice

# In[59]:


@dataclass()
class Rule:
    rule_id: str
    criteria: str
    operator: int
    value: int


# In[70]:


rule_1 = Rule("0001", "years_old", ">", 18)
rule_2 = Rule("0001", "years_old", ">", 18)


# Now, after comparing the two rules, we notice that they are actually equal. 

# In[61]:


rule_1 == rule_2


# Now, let us implement a "regular" class to see the difference. 

# In[62]:


class Rule:
    def __init__(self, rule_id, column_name, operator, value):
        self.rule_id = rule_id
        self.column_name = column_name
        self.operator = operator
        self.value = value


# BAAAMM!! It returns false. How can we fix this.
# 
# 

# In[64]:


rule_1 = Rule("0001", "years_old", ">", 18)
rule_2 = Rule("0001", "years_old", ">", 18)

rule_1 == rule_2


# As we can see, it is much less verbose to use dataclasses and besides that there are a lot of built-in "facilities" to help us manipulate data in Pyhton. 
# 
# In order to fix the Rule class, we'd have to implement a magic or **dunder** method `__eq__`

# In[65]:


class Rule:
    def __init__(self, rule_id: str, column_name: str, operator: str, value: int):
        self.rule_id = rule_id
        self.column_name = column_name
        self.operator = operator
        self.value = value

    def __eq__(self, other):
        return all(
            [
                self.rule_id == other.rule_id,
                self.column_name == other.column_name,
                self.operator == other.operator,
                self.value == other.value,
            ]
        )


# In[66]:


rule_1 = Rule("0001", "years_old", ">", 18)
rule_2 = Rule("0001", "years_old", ">", 18)

rule_1 == rule_2


# In[71]:


rule_1.__eq__(rule_2)


# ---
