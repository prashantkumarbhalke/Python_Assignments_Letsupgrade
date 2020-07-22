#!/usr/bin/env python
# coding: utf-8

# # Basic Python Syntax

# ## 1.Backslash:

# backslash is used for continuation
# 

# In[1]:


'''without backslash'''
print("hello 
      how are
      you")


# In[2]:


'''in order to deal with above situation we use continuation sign or backslash- with backslash'''
print("hello        how are        you")


# ## 2.Triple Quotes:
# 1.used to print multiline string as it is 
# 2.to make multiline comments in documents 
# 3.to write sql queries
# 

# In[3]:


print('''hello dear
how are you
how you doing''')


# In[4]:


'''Multiline
comments that vl not b executed
'''


# In[5]:


a='''
select * from table xyz
'''


# # # 3.String inside quotes
# using single,double quotes one inside other

# In[6]:


print('python's world')


# In[7]:


print("python's world")


# ## 4.Escape sequence of string
# used to print spaces inside a sting

# In[8]:


print('pythons\tworld')


# In[9]:


print('pythons\nworld')


# In[10]:


print('python\'s world')


# ## 5.formatted output
# how to print multiple statements inside print syntax ..?

# In[15]:


name='prashant'
marks=67.7867457
age=30


# In[16]:


print("the name is",name,"marks is",marks,"age is",age)


# In[17]:


print('the name is %s the marks is %f the age is %d'%(name,marks,age))


# In[19]:


print('the name is %10s the marks is %10f the age is %10d'%(name,marks,age))


# In[20]:


print('the name is %5s the marks is %10.2f the age is %5d'%(name,marks,age))


# In[22]:


print(f'the name is {name} marks is {marks} age is {age}')


# # python variables n assignment statements
# 

# In[25]:


a=10
b=10
id(a)
id(b)
id(a)==id(b)


# In[26]:


if=10


# In[27]:


_joke=90
print(_joke)


# In[28]:


10a=49


# In[29]:


_10=6
print(_10)


# In[30]:


bang_temp=88


# In[31]:


x=y=z=10


# In[32]:


x


# In[33]:


y


# In[34]:


id(x)==id(y)==id(x)


# In[35]:


del x


# In[36]:


x


# In[37]:


y


# In[38]:


z


# In[39]:


del y


# In[40]:


del z


# In[41]:


z


# In[42]:


3**3


# In[43]:


5//2


# In[44]:


5/2


# In[45]:


10/2


# In[46]:


10%3


# In[47]:


a=10
b=20
a==b


# In[48]:


c=10
a==c


# In[49]:


c<a


# In[50]:


c<=a


# In[51]:


c>=a


# In[52]:


c!=a


# In[53]:


12**=2


# In[54]:


10|4


# In[55]:


10&4


# In[56]:


a=240
b=1


# In[57]:


a|b


# In[58]:


bin(a)


# In[59]:


2>4 or 4>2


# In[60]:


3>2 and 5>4


# In[61]:


10>9 and 20>m


# In[62]:


10<9 and 20>m


# In[63]:


stri="python go"


# In[64]:


y in stri


# In[65]:


"y" in stri


# In[66]:


"a" in stri


# In[67]:


"h" in stri


# In[68]:


"h" not in stri


# In[69]:


a=10
b=10
a==b
id(a)==id(b)


# In[70]:


x=1.2
y=1.2
x is y


# In[71]:


id(x)==id(y)


# In[72]:


a=257
b=257
a is b


# In[73]:


10/20*4


# In[74]:


10+10/20*4


# In[75]:


2**-1


# In[76]:


10>8>9


# In[77]:


10<8>9


# In[ ]:




