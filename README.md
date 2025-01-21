# Image-Compressor
Using Lloyd's procedure for vector quantization to compress a photo by using fewer colors.

The goal is to reduce the number of distinct colors required to represent a photo, thereby allowing the photgraph to be greatly compressed (in a lossy manner) in future developments. 
After clustering, only k distinct colors are used, so each pixel can be represented by only $\lceil lg \textit{k} \rceil$ bits.

<div style="display: flex; justify-content: space-around; margin-bottom: 10px;">
  <img src="https://github.com/user-attachments/assets/daace162-8634-468d-bcef-ae9d8fdc9773" alt="Figure 1" width="500"/>
  <img src="https://github.com/user-attachments/assets/a5f8e1e3-fa3e-4aac-bb05-b2c1a096a36b" alt="Figure 2" width="500"/>
</div>
<div style="display: flex; justify-content: space-around;">
  <img src="https://github.com/user-attachments/assets/a639e9a0-30e0-4a1c-8569-c04eb005de82" alt="Figure 3" width="500"/>
  <img src="https://github.com/user-attachments/assets/acc5582c-0ca0-479f-ba24-012717e69dab" alt="Figure 4" width="500"/>
</div>
