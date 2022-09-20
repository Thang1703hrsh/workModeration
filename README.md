# Cơ sở lý thuyết:
- Makespan: Đối với M công việc và N tổ làm việc thì việc sắp xếp thời gian tối ưu nhất là cần thiết, và Makespan là thời gian tối ưu của 
công việc.
## Một số nguyên tắc chính trong sắp xếp thứ tự công việc:
- Công việc đặt hàng trước làm trước
- Công việc có thời gian giới hạn giao hàng trước làm trước
- Công việc có thời gian thực hiện ngắn nhất làm trước
- Công việc có thời gian dài nhất làm trước
- Tỷ lệ giới hạn: Công việc thực hiện tiếp theo là công việc có tỷ số thời gian đến ngày giao hàng
trên thời gian còn lại nhỏ nhất thì làm trước
- Chi phí chuyển đổi thấp
Một số nguyên tắc khác: Khách hàng quan trọng nhất, công việc có lợi nhuận cao nhất
- Chi phí chuyển đổi máy móc thấp nhất

## Các phương pháp chính heuristic: 
- FCFS: First Come First Served: Những đơn hàng hoặc công việc được đặt trước sẽ thực hiện trước
- EDD: Earliest Due Date: Đơn hàng nào có yêu cầu hoàn thành sớm nhất thì được ưu tiên làm trước
- SPT – Shortest Processing TimeL: Theo nguyên tắc này, công việc nào dự kiến làm nhanh nhất thì ưu tiên thực hiện trước, công việc nào lâu hơn sẽ thực hiện sau.
- LPT – Longest Processing Time: Theo nguyên tắc này người ta ưu tiên chọn công việc có thời gian gia công dài nhất để thực hiện trước và ngược lại.
- Slack: Theo nguyên tắc này trước tiên người ta xác định thời gian dư thừa giữa thời hạn hoàn thành và thời gian gia công, sau đó ưu tiên công việc có thời gian dư thừa nhỏ nhất trước.

## Các chỉ số cần thiết:
- Dòng thời gian: Khoảng thời gian sản phẩm từ khi công việc đưa vào cho tới khi hoàn thành
- Dòng thời gian lớn nhất: Tổng thời gian cần thiết để hoàn thành công việc
- Dòng thời gian trung bình: Thời gian trung bình của mỗi công việc
- Số công việc trung bình: = Tổng dòng thời gian/ Tổng thời gian gia công
- Thời gian hoàn thành trung bình = Tổng dòng thời gian / Số đơn hàng (số sản phẩm)
- Thời gian chậm trung bình = Tổng thời gian chậm/ Số đơn hàng (sản phẩm)
- Hiệu quả của phương pháp sắp xếp = Tổng thời gian thực hiện các công việc / Tổng dòng thời gian

## Tỉ số giới hạn:
Để kiểm tra xem công việc bố trí hợp lý không thì người ta dùng chỉ số giới hạn
CR = T / N
Trong đó: 
    - CR: Chỉ số giới hạn công việc i
    - T: Thời gian còn lại đối với công việc i 
    - N: Thời gian cần thiết để hoàn thành phần còn lại của công việc i

- Nếu CRi >1: Công việc i được hoàn thành trước thời hạn;
- Nếu CRi =1: Công việc i được hoàn thành đúng thời hạn;
- Nếu CRi <1: Công việc i không được hoàn thành đúng thời hạn.


## Các phương pháp giao công việc cho nhiều tổ: 
- Phương pháp Johnson:
    - Bước 1: Liệt kê thời gian cần thiết thực hiện từng công việc trên từng máy
    - Bước 2: Tìm công việc có thời gian thực hiện nhỏ nhất
    - Bước 3: Sắp xếp công việc: Nếu công việc vừa tìm được nằm trên máy 1 thì sắp xếp trước, nếu công việc này nằm trên máy 2 thì được sắp xếp cuối cùng. Khi một công việc đã được sắp xếp rồi thì ta loại trừ nó đi, chỉ xét những công việc còn lại.
    - Bước 4: Lặp lại bước 2 và 3 cho đến khi tất cả công việc được xếp hết
** Note: Không quá tối ưu, chỉ nên sử dụng trong 2-3 tổ bộ phận **

- Phương pháp Hungary:
    - Bước 1: Lập bảng phân việc và máy theo dữ liệu thực tế
    - Bước 2: Chọn công việc có thời gian nhỏ nhất trong từng hàng của bảng phân việc và lấy các số trong hàng trừ đi số đó
    - Bước 3: Từ bảng phân việc của bước 2, chọn công việc có thời gian nhỏ nhất trong từng cột và lấy các số trong cột trừ đi số đó
    - Bước 4. Tìm cách kẻ các đường thẳng đi qua hàng hoặc cột có các số 0 sao cho số đường thẳng kẻ được là ít nhất. Thực hiện như sau:
        - 4(a). Xét từng hàng của ma trận, nếu trong hàng có 1 số 0 thì khoanh tròn số 0 đó rồi gạch một đường thẳng xuyên suốt cột. Nếu điều kiện không thỏa mãn thì bỏ qua.
        - 4(b). Xét từng cột của ma trận, nếu trong cột có 1 số 0 thì khoanh tròn số 0 đó rồi gạch một đường thẳng xuyên suốt hàng. Nếu điều kiện không thỏa mãn thì bỏ qua. 4(c).
        - Lặp lại bước 4(a) và 4(b) đến khi khoanh hết tất cả các số 0.
        - Lưu ý. Nếu số đường thẳng kẻ được ít nhất bằng số hàng và số cột thì bài toán có lời giải tối ưu. Nếu số đường thẳng kẻ được nhỏ hơn số hàng và số cột thì chuyển xuống bước 5.

    - Bước 5: Khôi phục bảng phân việc (tạo thêm số 0). Tìm số nhỏ nhất trong các số không nằm trên các đường thẳng đã kẻ. Lấy các số không nằm trên đường thẳng đã kẻ trừ đi số đó. Cộng số nhỏ nhất đó với số nằm trên giao điểm các đường thẳng, còn các số khác giữ nguyên.

    - Bước 6: Lặp lại bước 4 và bước 5 cho đến khi nào khoanh tròn được n số 0 và cũng có n đường thẳng và bài toán có lời giải tối ưu.

## Các phương pháp của heuristic: 
1. Palmer heuristic: Tìm giá trị nhỏ nhất trong mỗi cột
    - Bước 1: Với N tổ, chúng ta sẽ giả sử N bộ số w sao cho tổ ở giữa luôn có giá trị 0, và 2 bên đối xứng, tức w mid = 0
            Qua J sản phẩm, mỗi sản phẩm sẽ được nhân với bộ số w giống mạng dense, Sinh ra cột pw chứa giá trị tổng của mỗi sản phẩm nhân với w
    - Bước 2: Sắp xếp bộ giá trị tổng pw giảm dần, khi đó được thứ tự công việc 
1.1 Phương pháp chặn dưới của Palmer heuristic (Lower Bound of Palmer Heuristic):
    - Bước 1: Tính tổng của mỗi cột, tức tính tổng thời gian làm tất cả các sản phẩm tại 1 tổ
    - Bước 2: Tính giá trị LB1 = Tổng cột 1 + min { Tổng các hàng của cột còn lại } (Với LB1 là giá trị tại cột đầu tiên)
    - Bước 3: Với LB2 là giá trị giữa = Tổng cột p2 + min {giá trị cột trước} + min {Tổng các hàng của các cột còn lại hoặc giá trị 1 cột sau}
              Với LBn là giá trị giữa = Tổng pn + min{Tổng các hàng của các cột trước} + min{Tổng các hàng của các cột sau}
    - Bước 4: Sau khi có {LB}: Tìm max của tập hợp LB
    
    Makespan = max LB 
2. NEH heuristic: 
    - Bước 1: Tính tổng p của mỗi hàng, tức thời gian làm mỗi sản phẩm
    - Bước 2: Sắp xếp chuỗi theo thứ tự giảm dần của tổng p (chuỗi F)
    - Bước 3: So sánh 2 sản phẩm và xét lại thứ tự, tổng thời gian làm cho hai sản phẩm và sắp xếp lại thứ tự sản phẩm
    - Bước 3: Xét vào chuỗi F ban đầu sau đó lấy sản phẩm tiếp theo của 2 sản phẩm trên đấy, giao hoán vị trí của sản phẩm thứ 3 và xét tổng thời 
    gian làm cho 3 sản phẩm, sắp xếp lại thứ tự sản phẩm thứ 3
    - Bước 4: Lặp lại Bước 3 cho tới khi hết sản phẩm

## Các phương pháp của metaheuristic: 
1. Tìm kiếm không gian trạng thái và thuật toán Simulated Annealing
    - Xét ví dụ: Có n thành phố A = {0,1,2,3,...,n}
    Thuật toán được trình bày như sau :

```
For t = 1 to m
1. Chọn ngẫu nhiên y ∈ N(x)
a) tính Δ(x,y) = Obj(y) – Obj(x) 
b) if Δ(x,y) < 0 then p = 1
c) else p = exp(−Δ(x,y)/T)
d) if rand[0,1] < p then x ← y. // lời giải y tốt hơn x
e) if Obj(x) < Obj(x*) then x* ← x // chuyển sang y với xác suất p. 

2. giảm T theo sơ đồ C
return x* //x* là trạng thái tốt nhất trong số những trạng thái đã xem xét
```

2. Thuật toán trâu bò Brute force
Nhược điểm: Thời gian tính toán lâu, lượng dữ liệu lớn khó có thể giải quyết nhanh chóng được
Ưu điểm: Dễ sử dụng


## Tham khảo: 
- https://lytuong.net/dieu-do-san-xuat/
- https://arxiv.org/ftp/arxiv/papers/1407/1407.5931.pdf#:~:text=The%20flowshop%20scheduling%20problem%20is,permutation%20flowshop%20sequencing%20production%20environment.

