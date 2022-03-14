create view HNfiltered
as
select * 
from HN
where [Giá (tỷ đồng)] >= 1
and [Giá (tỷ đồng)] <= 6
and [Số phòng ngủ] not like '1 phòng'
and [Quận/Huyện] not like 'Huyện%'
and [Phường/Xã] not like 'Xã%';

