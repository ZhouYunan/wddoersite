/**
 * Created by wddoer on 2015/5/15.
 */


//  设置时间显示，在base.html中调用
function ShowTime(){
    var NowDate = new Date();
    var NowHour = NowDate.getHours();
    var NowMinute = NowDate.getMinutes();
    var NowSecond = NowDate.getSeconds();
    document.getElementById('nowtime').innerHTML ='现在时间：' + NowHour + ':' + NowMinute + ':' + NowSecond;
    setTimeout('ShowTime()', 1000);
}