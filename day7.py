# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)

random_removed = st.pop()
print(random_removed)
removed = st.remove('item3')

print(st)

st.add('item6')
st.update({'item7', 'item8'})

st_2 = {'item1', 'item2', 'item3', 'item4'}
st_3 = {'item1', 'item2', 'item3', 'item4', 'item5'}
