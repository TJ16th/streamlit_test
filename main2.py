import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("streamlit 超入門")

st.write('DataFrame')

st.write('Display Image')

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


