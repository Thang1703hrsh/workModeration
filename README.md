# Cơ sở lý thuyết:
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















## Tham khảo: https://lytuong.net/dieu-do-san-xuat/
