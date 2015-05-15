/**
 * Created by wddoer on 2015/5/15.
 */


//  设置时间显示，在base.html中调用
function ShowTime(){
    var NowDate = new Date();
    var NowHour = NowDate.getHours();
    var NowMinute = NowDate.getMinutes();
    var NowSecond = NowDate.getSeconds();
    document.getElementById('nowtime').innerHTML ='现在时间：' + (NowHour<10?('0'+NowHour):NowHour) + ':' + (NowMinute<10?('0'+NowMinute):NowMinute) + ':' + (NowSecond<10?('0'+NowSecond):NowSecond);
    setTimeout('ShowTime()', 1000);
}