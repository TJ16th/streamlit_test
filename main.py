import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("streamlit 超入門")

st.write('プログレスバーテスト')
'start!'

latest_iterration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iterration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)
    

st.write('DataFrame')

st.write('Display Image')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは→カラムだよ')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.text_input('hogeee')

text = st.text_input('あなたの趣味を教えて下さい')
'あなたの趣味は',text,'です'

option = st.selectbox(
    '好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数字は', option, 'です。'

if st.checkbox('Show Image'):
    img = Image.open('p_value.jpg')
    st.image(img, caption='peach', use_column_width=True)

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)

st.map(df3)

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.area_chart(df2)

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as no
import pandas as pd
```
"""


