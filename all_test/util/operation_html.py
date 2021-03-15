import re
import os


class OperationHtml:
    def __init__(self, file_name, html=None, is_write=False):
        if is_write:
            project_file_name = "all_test/temp_html/" + file_name
            with open(project_file_name, 'w', encoding='utf-8') as file:
                file.write(html)
                self.html = html
                self.root_path = os.path.abspath(os.path.dirname(__file__)).split('all_test')[
                                0] + 'all_test/all_test/temp_html/' + file_name
                file.close()

        else:
            with open(file_name, 'r', encoding='utf-8') as file:
                message = file.read()
                self.html = message

    def GetValue(self, type, value):
        id = type + '="' + value + '"'
        out = re.findall(id + '(?:.|\n)*?>', self.html)
        # 如果没找到，可能是type是由单引号包围的
        if len(out) == 0:
            id = type + "='" + value + "'"
            out = re.findall(id + "(?:.|\n)*?>", self.html)
        value = []
        for i in out:
            print("1:", i)
            num = re.findall(r'value=\"(?:.|\n)*?\"', str(i))
            # 如果没找到，可能是value是由单引号包围的
            if len(num) == 0:
                num = re.findall(r"value=\'(?:.|\n)*?\'", str(i))
            if len(num) != 0:
                print("2:", num)
                str_value_temp = str(num[0]).split('=')[1]
                value.append(str_value_temp[1:len(str_value_temp) - 1])
            else:
                pass

        if len(value) == 0:
            value.append("")
        return value

    def get_root_path(self):
        return self.root_path


if __name__ == '__main__':
    str1 = '''						













<!DOCTYPE html>
<html style="overflow-x:auto;overflow-y:auto;">
<head>
	<title>出库实提登记 - Powered ZTDS</title>
	<meta http-equiv="Content-Type" content="text/html;charset=utf-8" /><meta name="author" content="http://jeesite.com/"/>
<meta name="renderer" content="webkit"><meta http-equiv="X-UA-Compatible" content="IE=8,IE=9,IE=10" />
<meta http-equiv="Expires" content="0"><meta http-equiv="Cache-Control" content="no-cache"><meta http-equiv="Cache-Control" content="no-store">
<!-- [扩展JS] 
<script type="text/javascript" src="/static/extJs.js" charset="utf-8"></script>-->

<script src="/static/jquery/jquery-1.8.3.min.js" type="text/javascript"></script>

<!-- [EasyUI]
<link id="easyuiTheme" rel="stylesheet" type="text/css" href="/static/easyui/themes/gray/easyui.css" /> -->
<link id="easyuiTheme" rel="stylesheet" type="text/css" href="/static/easyui/themes/icon.css" />
<link rel="stylesheet" type="text/css" href="/static/easyui/EasyUI/easyui.css" />
<script type="text/javascript" src="/static/easyui/jquery.easyui.min.js" charset="utf-8"></script>
<script type="text/javascript" src="/static/easyui/locale/easyui-lang-zh_CN.js" charset="utf-8"></script>



<link href="/static/bootstrap/2.3.1/css_cerulean/bootstrap.css" type="text/css" rel="stylesheet" />
<script src="/static/bootstrap/2.3.1/js/bootstrap.js" type="text/javascript"></script>
<link href="/static/bootstrap/2.3.1/awesome/font-awesome.min.css" type="text/css" rel="stylesheet" />
<!--[if lte IE 7]><link href="/static/bootstrap/2.3.1/awesome/font-awesome-ie7.min.css" type="text/css" rel="stylesheet" /><![endif]-->
<!--[if lte IE 6]><link href="/static/bootstrap/bsie/css/bootstrap-ie6.min.css" type="text/css" rel="stylesheet" />
<script src="/static/bootstrap/bsie/js/bootstrap-ie.min.js" type="text/javascript"></script><![endif]-->
<link href="/static/jquery-select2/3.4/select2.css" rel="stylesheet" />
<script src="/static/jquery-select2/3.4/select2.min.js" type="text/javascript"></script>
<script src="/static/jquery-select2/3.4/linkage.js" type="text/javascript"></script>
<link href="/static/jquery-validation/1.11.0/jquery.validate.min.css" type="text/css" rel="stylesheet" />
<script src="/static/jquery-validation/1.11.0/jquery.validate.min.js" type="text/javascript"></script>
<script src="/static/jquery-validation/1.11.0/additional-methods.js" type="text/javascript"></script>
<link href="/static/jquery-jbox/2.3/Skins/Bootstrap/jbox.min.css" rel="stylesheet" />
<script src="/static/jquery-jbox/2.3/jquery.jBox-2.3.min.js" type="text/javascript"></script>
<script src="/static/My97DatePicker/WdatePicker.js" type="text/javascript"></script>

<script src="/static/common/mustache.min.js" type="text/javascript"></script>
<link href="/static/common/zmd.css" type="text/css" rel="stylesheet" />
<script src="/static/common/zmd.min.js" type="text/javascript"></script>
<script type="text/javascript">var ctx = '/a', ctxStatic='/static',ctxDownload = '/download',upload_completed=0,
tabmode = 1;
</script>

<link href="/static/bootstrap/2.3.1/css_cerulean/fixed_table_rc.css" type="text/css" rel="stylesheet" />
<script src="/static/bootstrap/2.3.1/js/fixed_table_rc.js" type="text/javascript"></script>
<script src="/static/moduleCommon/ganged.js" type="text/javascript"></script>
<script src="/static/moduleCommon/hrefTab.js" type="text/javascript"></script>
<link rel="shortcut icon" href="/static/images/favicon.ico" type="image/x-icon" />
<script src="/static/moduleCommon/setPageNum.js" type="text/javascript"></script>
<script src="/static/moduleCommon/trHighLight.js" type="text/javascript"></script>
		
	
	
	<meta name="decorator" content="default"/>
	<script type="text/javascript" src="/static/doT/doT.js"></script>
	<script src="/static/common/computer.js" type="text/javascript"></script>
	<script src="/static/moduleCommon/enter/maintianWorkload.js" type="text/javascript"></script>
	<script src="/static/moduleCommon/send/inputCombo.js" type="text/javascript"></script>
	<link id="easyuiTheme" rel="stylesheet" type="text/css" href="/static/easyui/themes/gray/easyui.css" />
	<script type="text/javascript" src="/static/extends.js" charset="utf-8"></script>
	<style type="text/css">.table-striped tbody>tr.editing{    background-color: rgb(170, 201, 255); 
	select, textarea, input[type="text"], input[type="password"], input[type="datetime"], input[type="datetime-local"], input[type="date"], input[type="month"], input[type="time"], input[type="week"], input[type="number"], input[type="email"], input[type="url"], input[type="search"], input[type="tel"], input[type="color"], .uneditable-input {

font-size: 12px;

}
	}
	.table-striped tbody>tr>td{white-space:nowrap}
	
	</style>
	<script type="text/javascript">
	function clearContractOwner(){
		$("#contractOwnerIdIp").select2('data','');
	}
	function getWeigtTotal(){
		return $('#relWeightTd').text();
	}
		$(document).ready(function() {
			$.extend($.validator.defaults);
			$("#inputForm").validate({
				rules:{
					/* applyMoney:{checkNumRule:[11,2]}, */
				},
				messages:{},
				submitHandler: function(form) {	
					$("#submitPrintBt").attr("disabled",true);
					$("#submitBt").attr("disabled",true);
					var msg='';
					msg =validateBaseForm(msg);
					msg = checkWorkLoadMsg(msg);
					if(msg!=''){						
						$.jBox.error(msg, '提示信息');
						$("#submitPrintBt").removeAttr("disabled");
	         			$("#submitBt").removeAttr("disabled");
						return false;
					}
					if(hasWorkload()){
						var chk = checkWorkload();
						if(chk == -1) {
							submitData();
						} else {
							top.$.jBox.confirm('工作量大于总的业务量，是否继续提交?',"系统提示",function(v,h,f){
								if(v=="ok"){
									submitData();
								}else{
									clearWorkload(chk);
									tabShow('workloadTabLi', 'workloadDiv');
									$("#submitPrintBt").removeAttr("disabled");
				         			$("#submitBt").removeAttr("disabled");
								}
							},{buttons:{'继续': 'ok','取消':'xx'},persistent: true});
						}	
					}else{
						top.$.jBox.confirm('本次出库未添加工作量信息，是否继续提交',"系统提示",function(v,h,f){
							if(v=="ok"){
								submitData();
							}else{
								$("#submitPrintBt").removeAttr("disabled");
			         			$("#submitBt").removeAttr("disabled");
								return;
							}
						},{buttons:{'继续': 'ok','取消':'xx'},persistent: true});
					}
					return false;
				},
				errorContainer: "#messageBox",
				errorPlacement: function (error, element) {
					$("#messageBox").text("输入有误，请先更正。");
					if (element.is(":checkbox")||element.is(":radio")||element.parent().is(".input-append")){
						error.appendTo(element.parent().parent());
					} else {
						error.insertAfter(element);
					}
				}
			});
			calcuTotal();
			var contractOwnerId = '';
			if (contractOwnerId== null || contractOwnerId=='') {
				linkContractOwnerId('3271');
			}		
		});
		
		//提交
		function submitData() {
			var params=$("#inputForm").serialize();
			$.post('/a/output/proOutput/isOverWeight',params,function(rsp){
				if(!rsp.status){
					$.jBox.error("已超过实提监控设置，请核实！", '提示');
					$("#submitPrintBt").removeAttr("disabled");
         			$("#submitBt").removeAttr("disabled");
					return;
				}else{
					var saveUrl=$("#inputForm").attr('action');
					$.ajax({
		                cache: true,
		                type: "POST",
		                url:saveUrl,
		                data:$('#inputForm').serialize(),
		                beforeSend: function(){
							loadingAndWait('正在提交，请稍等...');
					    },
					    complete: function(){
		                	top.$.jBox.closeTip();                 
		                },
		                success: function(ret) {
		                   if(ret.status){//成功跳转列表页
		                	   top.$.jBox.closeTip();
		                   		if(ret.other) top.$.fn.tabJumpJump('出库实提登记','出库管理',true,'tab=2&printId='+ret.other);
		                   		else top.$.fn.tabJumpJump('出库实提登记','出库管理',true,'tab=2');
		                   }else{
		                	   $("#submitPrintBt").removeAttr("disabled");
		                	   $("#submitBt").removeAttr("disabled");
		                	   top.$.jBox.closeTip();
		                	   alertx(ret.msg);
		                   }
		                },
		                error: function(XMLHttpRequest, textStatus, errorThrown) {
			            	alertx("未知错误:"+XMLHttpRequest.status+"	textStatus:"+textStatus);
	                        $("#submitPrintBt").removeAttr("disabled");
		         			$("#submitBt").removeAttr("disabled");
			            	top.$.jBox.closeTip();
	                    }
		            });
				}
			},'json').error(function() {
				$("#submitPrintBt").removeAttr("disabled");
     			$("#submitBt").removeAttr("disabled");
				alertx("操作失败！请联系系统管理员。");
			});
		}
		
		//输入限制(tab键问题修改)
		function clearNoNum(obj,e){ 
		   /*  obj.value = obj.value.replace(/[^\d.]/g,"");  //清除“数字”和“.”以外的字符  
		    obj.value = obj.value.replace(/\.{2,}/g,"."); //只保留第一个. 清除多余的  
		    obj.value = obj.value.replace(".","$#$").replace(/\./g,"").replace("$#$","."); 
		    obj.value = obj.value.replace(/^(\-)*(\d+)\.(\d\d\d).*$/,'$1$2.$3');//只能输入两个小数  
		    if(obj.value.indexOf(".")< 0 && obj.value !=""){//以上已经过滤，此处控制的是如果没有小数点，首位不能为类似于 01、02的金额 
		        obj.value= parseFloat(obj.value); 
		    } */
		    
		    /* if(!validateNum(obj.value,9,3)){
		    	return false;
		    } */
		    var e = window.event;
		    var keyCode = e.keyCode;
		    //删除 以及tab
		    if (keyCode >= 8 && keyCode <= 9 )return true;
			// 数字
		    if (keyCode >= 46 && keyCode <= 57 ) return true;
		    // 小数字键盘
		    if (keyCode >= 96 && keyCode <= 105) return true;
		    if(keyCode==110||keyCode==190){
		    	if(obj.value.indexOf(".")< 0) return true;
		    }
		    e.returnValue = false;
		    return false;
		}
		//输入限制
		function clearNoNum2(obj,e){ 
		   /*  obj.value = obj.value.replace(/[^\d.]/g,"");  //清除“数字”和“.”以外的字符  
		    obj.value = obj.value.replace(/\.{2,}/g,"."); //只保留第一个. 清除多余的  
		    obj.value = obj.value.replace(".","$#$").replace(/\./g,"").replace("$#$","."); 
		    obj.value = obj.value.replace(/^(\-)*(\d+)\.(\d\d\d).*$/,'$1$2.$3');//只能输入两个小数  
		    if(obj.value.indexOf(".")< 0 && obj.value !=""){//以上已经过滤，此处控制的是如果没有小数点，首位不能为类似于 01、02的金额 
		        obj.value= parseFloat(obj.value); 
		    } */
		    
		    /* if(!validateNum(obj.value,9,3)){
		    	return false;
		    } */
		    var e = window.event;
		    var keyCode = e.keyCode;
		    //删除 以及tab
		    if (keyCode >= 8 && keyCode <= 9 )return true;
			// 数字
		    if (keyCode >= 46 && keyCode <= 57 ) return true;
		    // 小数字键盘
		    if (keyCode >= 96 && keyCode <= 105) return true;
		    e.returnValue = false;
		    return false;
		}
		
		//计算总计
		function calcuTotal(){
			var allRealNum = $(".realNumIp");
			var allRealWeight = $(".realWeightIp");
			var realNumCount =0;
			var realWeightCount =0;
			for(var i=0;i<allRealNum.length;i++){
				realNumCount = accAdd(realNumCount, allRealNum.eq(i).val());
			}
			for(var i=0;i<allRealWeight.length;i++){
				realWeightCount = accAdd(realWeightCount, allRealWeight.eq(i).val());
			}
			$("#realNumTotal").text(realNumCount);
			$("#relWeightTd").text(realWeightCount.toFixed(3));
		}
		
		//检查实提数量：如有发货单，不能超过发货单的 应发数量    如无发货单，新增：不能超过库存可用数量  改单：不能超过库存可用数量+原实提单的实提数量
		function checkRealNum(obj) {
			var realNum = $(obj).val();			
			var $curTr = $(obj).parent().parent();
			var isFromInventory = $curTr.find("[name='isFromInventory']").val();
			var oldNum = $curTr.find("[name='oldOutputNum']").val(); //应发数量
			var supplyNum = $curTr.find("[name='supplyNum']").val();
			var oldRealNum = $curTr.find("[name='oldRealNum']").val(); //改单 原实提数量
			var outputId = $("#id").val();
			if(realNum!='' && !validateNum(realNum,11,0)){
				$.jBox.error("实提数量应为正整数！", '提示');
				$(obj).val("");
				return;
			} 
			if (isFromInventory == "1") {
				if (outputId == null || outputId == "") {
					if (parseInt(realNum) > parseInt(supplyNum)) {
						$.jBox.error("实提数量不能超过可用数量！", '提示');
					}
				} else {
					if (parseInt(realNum) > accAdd(supplyNum, oldRealNum)) {
						$.jBox.error("实提数量不能超过可用数量！", '提示');
					}
				}				
			} else {
				if (parseInt(realNum) > parseInt(oldNum)) {
					$.jBox.error("实提数量不能超过应发数量！", '提示');
				}
			}
			var realWeightIp = $curTr.find(".realWeightIp");
			var invNum = $curTr.find(".numIh").val();
			if(realNum==invNum){
				realWeightIp.val($curTr.find(".weightIh").val());
				return;
			}
			var averageWeight = $curTr.find(".averageWeightIh").val();
			
			realWeightIp.val(accMul(realNum,averageWeight).toFixed(3));
		}
		
		//检查实提重量：新增出库单：不能超过发货单的 应发重量+库存的可供量； 改单：不能超过 原单的实提重量+库存可供量
		//2018.1.17 统一为：实提重量不能超过库存实际重量 (新增：实提重量不能超过库存实际重量； 改单：不能超过 原单的实提重量+库存实际重量)
		function checkRealWeight(obj) {
			var realWeight = $(obj).val();
			var $curTr = $(obj).parent().parent();
			//var oldWeight = $curTr.find("[name='oldOutputWeight']").val(); //应发重量
			var weight = $curTr.find("[name='weight']").val();  //实际重量，不是可用量
			var oldRealWeight = $curTr.find("[name='oldRealWeight']").val(); //改单 原实提重量
			var outputId = $("#id").val();
			if(realWeight!='' && !validateNum(realWeight,11,3)){
				$.jBox.error("实提重量应为最多三位小数的正数！", '提示');
				$(obj).val("");
				return;
			} 
			if (outputId == null || outputId == "") {
				if (parseFloat(realWeight) > parseFloat(weight)) {
					$.jBox.error("实提重量不能超过库存重量！", '提示');
				}
			} else {
				if (parseFloat(realWeight) > accAdd(oldRealWeight, weight)) {
					$.jBox.error("实提重量不能超过库存重量！", '提示');
				}
			} 
		}
		
		//页面Check
		function validateBaseForm(msg,verify) {
			//出库时间不能早于发货时间
			var sendDate = $("#sendDate").val();
			var outputDate = $("#outputDate").val();
			if(sendDate != "" && outputDate != ""){
				if(outputDate < sendDate){
					msg+='出库时间不能早于发货时间!';
					return msg;
				}
			}
			var deliverName =$("#deliverName").val();
			if(deliverName == "" ){
					msg+='提货人不能为空!';
					return msg;
			}
			//Check 实提数量和实提重量
			var totalSendNum = 0;
			var totalRealNum = 0;
			var dataTrArr = $("#dataArea tr");
			var outputId = $("#id").val(); //实提ID 改单用
			for(var i=0; i<dataTrArr.length; i++) {
				var dataTr = dataTrArr.eq(i);
				var isFromInventory = dataTr.find("[name='isFromInventory']").val();
				var oldNum = dataTr.find("[name='oldOutputNum']").val(); //应发数量
				var supplyNum = dataTr.find("[name='supplyNum']").val(); //库存可供数量
				var oldRealNum = dataTr.find("[name='oldRealNum']").val(); //原实提数量 改单用
				var realNum = dataTr.find("[name='realNum']").val(); 
				var weight = dataTr.find("[name='weight']").val(); //库存实际重量
				var oldRealWeight = dataTr.find("[name='oldRealWeight']").val(); //原实提重量 改单用
				var realWeight = dataTr.find("[name='realWeight']").val();
				if(realNum!='' && !validateNum(realNum,11,0)){
					msg+='实提数量应为正整数！';
					return msg;
				} 
				if(realWeight!='' && !validateNum(realWeight,11,3)){
					msg+='实提重量应为最多三位小数的正数！';
					return msg;
				} 
				if (isFromInventory == "1") {
					if (outputId == null || outputId == "") {
						if (parseInt(realNum) > parseInt(supplyNum)) {
							msg+='实提数量不能超过可用数量！';
							return msg;
						}
					} else {
						//改单
						if (parseInt(realNum) > accAdd(supplyNum, oldRealNum)) {
							msg+='实提数量不能超过可用数量！';
							return msg;
						}
					}					
				} else {
					if (parseInt(realNum) > parseInt(oldNum)) {
						msg+='实提数量不能超过应发数量！';
						return msg;
					}
				}
				if (outputId == null || outputId == "") {
					if (parseFloat(realWeight) > parseFloat(weight)) {
						msg+='实提重量不能超过库存重量！';
						return msg;
					}
				} else {
					//改单
					if (parseFloat(realWeight) > accAdd(oldRealWeight, weight)) {
						msg+='实提重量不能超过库存重量！';
						return msg;
					}
				}				
				totalSendNum = parseInt(totalSendNum) + parseInt(oldNum);
				totalRealNum = parseInt(totalRealNum) + parseInt(realNum);
			}
			//总实提数量不能超过总的发货数量
			if (parseInt(totalRealNum) > parseInt(totalSendNum)) {
				msg+='实提总数量不能超过应发总数量！';
				return msg;
			}
			if (verify!=1) {
				var updateReason = $("#updateReason").val();
				if(updateReason==''){
					msg+='*【变更原因】不能为空；</br>'
				}
			}
			return msg;
		}
		
		function operateType(oType) {
			if(oType){
				$("#inputForm").attr('action','/a/output/proOutput/save?andPrint=true')
			}else{
				$("#inputForm").attr('action','/a/output/proOutput/save')
			}
			$("#inputForm").submit();
		}
		
		function cancelClose() {
			//  多页签模式
			top.$.fn.jerichoTab.closeCurrentTab();
			//
			// 
		}
		
		//删除选择的资源
		function delRes(){			
			var arr = $("input[name='sltRD']:checked");
			if(arr == null || arr.length == 0){
				alertx('请选择一条数据');
				return;
			}
			if($(".dataTr").length <= 1) {
				alertx('最后一条物资明细不能删除！');
				return;
			}
			arr.each(function(i){
				$(this).parent().parent().remove();
			});
			//重新计算总计
			calcuTotal();
		}
		
		//新增资源(品名 材质 规格 产地 货主 仓库 都相同的物料)
		function addSameRes(){
			var arr1 = $("input[name='sltRD']:checked");
			if(arr1 == null || arr1.length == 0) {
				alertx('请选择一条数据');
				return;
			}
			var ownerId = $('#ownerId').val();
			var warehouseId = $('#warehouseId').val();
			var ownerName =$('#ownerName').val();
			var inventoryId='';
			var brandId='';
			var textureId='';
			var specificationId='';
			var placesteelId='';
			//var param='';
			if(arr1.length>0){
				for(var i=0; i<arr1.length; i++){
					var ivtInfoArr = arr1.eq(i).val().split(',');					
					brandId=ivtInfoArr[0];
					textureId=ivtInfoArr[1];
					specificationId=ivtInfoArr[2];
					placesteelId=ivtInfoArr[3];				
				}				
			}
			//取页面所有库存ID
			var arr2 = $("input[name='sltRD']");
			if(arr2.length>0){
				for(var j=0; j<arr2.length; j++){
					var ivtArr = arr2.eq(j).val().split(',');					
					inventoryId+=ivtArr[4];
					if(j != arr2.length-1){
						inventoryId += ",";
					}
				}
			}
			//param = 'ownerId='+ownerId+'&warehouseId='+warehouseId+'&brandId='+brandId+'&textureId='+textureId+'&specificationId='+specificationId+'&placesteelId='+placesteelId+'&excludeIds='+inventoryId;
			
			var url = "/a/output/proOutput/toSltInventory";
			
			top.$.jBox("iframe:"+url, {
				ajaxData:{'ownerId':ownerId, 'warehouseId':warehouseId, 'brandId':brandId, 'textureId':textureId, 'specificationId':specificationId, 'placesteelId':placesteelId, 'excludeIds':inventoryId},
				title:"添加物料明细 - "+ownerName, width:1100,height:550, 
				buttons: { '提交': true,'关闭': false},
				submit:function(v,h,f){
					if(v){
						var arr = h.find("iframe")[0].contentWindow.$("input[type='checkbox']:checked");
						if(arr == null || arr.length == 0 ){//关闭弹框
							return true;
						}
						//本次选择的ids
						var includeIds = "";
						arr.each(function(i){
							includeIds+=$(this).val();
							if(i != arr.length-1){
								includeIds += ",";
							}
						});
						//后台取数据
						var params = {
							"ownerId":ownerId,
							'warehouseId':warehouseId,
							"includeIds":includeIds
						};
						$.post("/a/output/proOutput/getInventorys", params, function(data){
							var table1TmplFn = doT.template($("#dataTmpl").html())(data);
							$("#dataArea").append(table1TmplFn);							
							calcuTotal();
							return true;
						});
					}else{
						return true;
					}
				},
				loaded : function(h) {   //隐藏滚动条  
	                $(".jbox-content", top.document).css( "overflow-y", "hidden");   
	            }
			});
		}
		
		//新增资源(品名 材质 规格 货主 仓库都相同 产地不同的物料)
		function addRes(){
			var arr1 = $("input[name='sltRD']:checked");
			if(arr1 == null || arr1.length == 0) {
				alertx('请选择一条数据');
				return;
			}
			var ownerId = $('#ownerId').val();
			var warehouseId = $('#warehouseId').val();
			var inventoryId='';
			var brandId='';
			var textureId='';
			var specificationId='';
			//var param='';
			if(arr1.length>0){
				for(var i=0; i<arr1.length; i++){
					var ivtInfoArr = arr1.eq(i).val().split(',');					
					brandId=ivtInfoArr[0];
					textureId=ivtInfoArr[1];
					specificationId=ivtInfoArr[2];			
				}
			}
			//取页面所有库存ID
			var arr2 = $("input[name='sltRD']");
			if(arr2.length>0){
				for(var j=0; j<arr2.length; j++){
					var ivtArr = arr2.eq(j).val().split(',');					
					inventoryId+=ivtArr[4];
					if(j != arr2.length-1){
						inventoryId += ",";
					}
				}
			}
			//param = 'ownerId='+ownerId+'&warehouseId='+warehouseId+'&brandId='+brandId+'&textureId='+textureId+'&specificationId='+specificationId+'&excludeIds='+inventoryId;
			
			var url = "/a/output/proOutput/toSltDiffInventory";
			var ownerName =$('#ownerName').val();
			top.$.jBox("iframe:"+url, {
				ajaxData:{'ownerId':ownerId, 'warehouseId':warehouseId, 'brandId':brandId, 'textureId':textureId, 'specificationId':specificationId, 'excludeIds':inventoryId},
				title:"添加物料明细 - "+ownerName, width:1100,height:550, 
				buttons: { '提交': true,'关闭': false},
				submit:function(v,h,f){
					if(v){
						var arr = h.find("iframe")[0].contentWindow.$("input[type='checkbox']:checked");
						if(arr == null || arr.length == 0 ){//关闭弹框
							return true;
						}
						//本次选择的ids
						var includeIds = "";
						arr.each(function(i){
							includeIds+=$(this).val();
							if(i != arr.length-1){
								includeIds += ",";
							}
						});
						//后台取数据
						var params = {
							"ownerId":ownerId,
							'warehouseId':warehouseId,
							"includeIds":includeIds
						};
						$.post("/a/output/proOutput/getInventorys", params, function(data){
							var table1TmplFn = doT.template($("#dataTmpl").html())(data);
							$("#dataArea").append(table1TmplFn);							
							calcuTotal();
							return true;
						});
					}else{
						return true;
					}
				},
				loaded : function(h) {   //隐藏滚动条  
	                $(".jbox-content", top.document).css( "overflow-y", "hidden");   
	            }
			});
		}
	</script>

</head>
<body>
	















<script type="text/javascript">top.$.jBox.closeTip();</script>

<div class="bg_white_10">
<ul class="nav nav-tabs">
	<li id="basicTabLi" class="active"><a href="javascript:void(0);" onclick="tabShow('basicTabLi', 'basicDiv')">物料信息</a></li>
	<li id="spendTabLi"><a href="javascript:void(0);" onclick="tabShow('spendTabLi', 'spendDiv')">费用明细</a></li>
	<li id="workloadTabLi"><a href="javascript:void(0);" onclick="tabShow('workloadTabLi', 'workloadDiv')">工作量</a></li>
	<li id="annexTabLi"><a href="javascript:void(0);" onclick="tabShow('annexTabLi', 'annexDiv')">附件</a></li>
</ul>
<form id="inputForm" class="form-horizontal" action="/a/output/proOutput/save" method="post">
<div id="basicDiv" class="tabDiv">
	<input id="id" name="id" type="hidden" value=""/>
	<input id="sendId" name="sendId" type="hidden" value="65084"/>
	<input id="confirmId" name="confirmId" type="hidden" value=""/>
	<input id="outputCode" name="outputCode" type="hidden" value=""/>
	<input id="officeId" name="officeId" type="hidden" value="2"/>
	<input type="hidden" name="sendDate" id="sendDate" value="2020-12-14 00:01"/>
	<input type="hidden" id="isNewDeliveryCompany" name="isNewDeliveryCompany" value="1"/>
	<!-- <input type="hidden" id="deliveryCompany"  name="deliveryCompany" /> -->
	<input id="deliveryCompany" name="deliveryCompany" type="hidden" value="测试货主"/>
	<input type="hidden" id="isNewDriverIp"  name="isNewDriverIp" value="1"/>
	<!-- <input type="hidden" id="cardNo" />
	<input type="hidden" id="carPlateNo"/>
	<input type="hidden" id="driverId"  name="driverId" />
	<input type="hidden" id="deliverName" name="deliverName" /> -->
	
	<input id="driverId" name="driverId" type="hidden" value="7233"/>
	<input id="deliverName" name="deliverName" type="hidden" value="唐顺意"/>
	<span id="spenderNameTd" style="display:none">测试公司</span>
	<div class="cone">
	<div class="titleArea">基本信息</div>
	<div class="bg_white_10_tn" style="margin-bottom:10px;">
		<table class="searchui">
			<tr>
				<th><font color="red">*</font>发货单号</th>
				<td>
	            	<input id="sendCode" name="sendCode" class="input-medium" readonly="readonly" type="text" value="FH20121460302"/>
	            </td>
	            <th><font color="red">*</font>出库日期</th>
				<td>
				
		           
	            	<input id="outputDate" name="outputDate" type="text" readonly="readonly" maxlength="20" class="input-xlarge Wdate Wdatetime required billDateInput"
						value="2020-12-14 12:55"
						onclick="WdatePicker({dateFmt:'yyyy-MM-dd HH:mm',isShowClear:false});" onchange="clearContractOwner();"/>
					 
		           
		           
	            </td>
	            <th><font color="red">*</font>提单号</th>
	            <td>
	            	<input id="ladingCode" name="ladingCode" class="input-medium" type="text" value="AutoTest"/>
	            </td>
	            <th><font color="red">*</font>货主单位</th>
	            <td>
	            	<input id="ownerName" name="ownerName" class="input-large" readonly="readonly" type="text" value="测试公司"/>
					<input id="ownerId" name="ownerId" type="hidden" value="3271"/>
	            </td>
			</tr>
			<tr>
				<th><font color="red">*</font>提货单位</th>
				<td class="input-medium required">
	            	
	            	<select class="easyui-combobox" id="deliveryCompanyIp" style="width:118px;"   >  
	    			</select>
	            </td>
	            <th><font color="red">*</font>提货人</th>
				<td class="input-medium required" >
	            	
					<select class="easyui-combobox required" id="driverIp" style="width:118px;"   >  
	    			</select>
	            </td>
	            <th><font color="red">*</font>证件号</th>
	            <td>
	            	
	            	<input id="cardNo" name="cardNo" class="input-medium required" type="text" value="430482199711270371"/>
	            </td>
	            <th><font color="red">*</font>车牌号</th>
	            <td>
	            	
	            	<input id="carPlateNo" name="carPlateNo" class="input-medium required" type="text" value="湘D666666"/>
	            </td>
			</tr>
			<tr>
				<th><font color="red">*</font>出库方式</th>
				<td>
	            	
					<select id="sendMode" name="sendMode" class="input-medium required">
						<option value="01">抄码出库</option><option value="02" selected="selected">过磅出库</option><option value="03">理计出库</option>
					</select>
	            </td>
	            <th><font color="red">&nbsp;</font>结算单位</th>
				<td>
					<input id="spenderIdIp" name="spenderId" delayedSrc="/a/sys/sysCustomer/getCustomerNameJson" class="input-medium delay" delayedMinInput="0" dataFunc="buildOnlyCostCompParams" onchange="ownLinkPaymentMode(this.value);linkContractOwnerId(this.value);" type="text" value="3271"/>
	            	
	            </td>
	            <th><font color="red"></font>计费合同</th>
			    <td>
	           		<input id="contractOwnerIdIp" name="contractOwnerId" delayedSrc="/a/sys/sysCustomer/getCustomerNameJson" class="input-medium delay" delayedMinInput="0" dataFunc="buildOnlyCustomerParams1" type="text" value=""/>
			    </td>
	            <th><font color="red">*</font>结算方式</th>
	            <td>
	            	
					<select id="paymentMode" name="paymentMode" class="input-medium">
						<option value="2" selected="selected">月结</option><option value="1">现结</option>
					</select>
	            </td>
			</tr>
			<tr>
				<th><font color="red">*</font>所属仓库</th>
	            <td>
	            	<input id="warehouseName" name="warehouseName" class="input-large" readonly="readonly" type="text" value="测试仓库"/>
					<input id="warehouseId" name="warehouseId" type="hidden" value="122"/>
	            </td>
				<th><font color="red">&nbsp;</font>制单员</th>
				<td>
	            	<input type="text" readonly="readonly" class="input-medium" value="自动化测试"/>
	            </td>
	            <th><font color="red">&nbsp;</font>备注</th>
				<td>
	            	<input id="remarks" name="remarks" class="input-large" type="text" value=""/>
	            </td>	            
			</tr>
		</table>
	</div>
	</div>
	<div class="clearfix"></div>
	<div class="cone">
	<div class="titleArea">物料明细
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		
			<input class="btn btn-primary" type="button" onclick="addSameRes();" value="批次添加"/>&nbsp;
		
		
			<input class="btn btn-primary" type="button" onclick="addRes();" value="物料添加"/>&nbsp;
		
		
			<input class="btn btn-primary"  type="button" onclick="delRes();" value="删除"/>
		
	</div>
		<ul class="cone ul-form floatLi" id="guaMaterialUl" style="padding:0;margin-left: -1px;">
		<div class="bg_white_10" style="overflow-x: scroll;">
		<table id="materialTable" class="table table-striped table-bordered table-condensed">
			<thead>
			<tr>
				<th style='text-align:center;'>选择</th>
				<th>品名 规格 材质 产地</th>
				<!-- <th>提单数量</th>
				<th>提单重量</th> -->
				<!-- <th>支</th> -->
				<th>实物数量</th>
				<th>实物重量</th>
				<th>应发数量</th>
				<th>应发重量</th>
				<th>实提数量</th>
				<th>实提重量</th>					
				<th>捆包号</th>
				<th>合同号</th>
				<th>库位</th>
				<th>层号</th>
				<th>货物编号</th>
				<th>车船号</th>
				<th>资源号</th>
				<th>计量方式</th>
				<th>入库时间</th>
				<th>加工单号</th>
				<th>总车数</th>
				<th>备注</th>
			</tr>
			</thead>
			<tbody id='dataArea'>				
			
				<tr class="dataTr" idx="0" name="material">			
					<td>
						<input type="radio" name="sltRD" value="2,2,2,2,90582"/>
						<input type="hidden" name="detailId" class="idIh" value=""/>
						<input type="hidden" name="brandId" class="brandIdIh" value="2"/>
						<input type="hidden" name="textureId" class="textureIdIh" value="2"/>
						<input type="hidden" name="specificationId" class="specificationIdIh" value="2"/>
						<input type="hidden" name="placesteelId" class="placesteelIdIh" value="2"/>
						<input type="hidden" name="materialDesc" class="materialDescIh" value="螺纹钢 Φ12MM*9 HRB400 安源"/>
						<input type="hidden" name="warehousePlaceId" class="warehousePlaceIdIh" value="1"/>
						<input type="hidden" name="outputNumUnit" class="outputNumUnitIh" value="01"/>
						<input type="hidden" name="outputWeightUnit" class="outputWeightUnitIh" value="01"/>
						<input type="hidden" class="averageWeightIh" value="1.0"/>
						<input type="hidden" name="realNumUnit" class="realNumUnitIh" value="01"/>
						<input type="hidden" name="realWeightUnit" class="realWeightUnitIh" value="01"/>							
						<input type="hidden" name="inventoryId" class="inventoryIdIh" value="90582"/>
						<input type="hidden" name="sendDetailId" class="sendDetailIdIh" value="2677124"/>
						<input type="hidden" name="ladingDetailId" class="ladingDetailIdIh" value=""/>
						<input type="hidden" name="oldPiece" class="oldPieceIh" value=""/>
						<input type="hidden" name="oldOutputNum" class="oldOutputNumIh" value="2"/>
						<input type="hidden" name="oldOutputWeight" class="oldOutputWeightIh" value="2.0"/>
						<input type="hidden" name="supplyWeight" class="supplyWeightIh" value="2.0"/>
						<input type="hidden" name="supplyNum" class="supplyNumIh" value="2"/>
						<input type="hidden" name="weight" class="weightIh" value="2.0"/>
						<input type="hidden" name="num" class="numIh" value="2"/>
						<input type="hidden" name="oldRealWeight" class="oldRealWeightIh" value="2.0"/>
						<input type="hidden" name="oldRealNum" class="oldRealNumIh" value="2"/>
						<input type="hidden" name="isFromInventory" class="isFromInventoryIh" value="0"/>
						<input type="hidden" name="isScan" class="isScanIh" value="0"/>
						<input type="hidden" name="enterDate" class="enterDateIh" value="2020-12-14 00:01" />
					</td>
					<td class="materialDescTd">螺纹钢 Φ12MM*9 HRB400 安源</td>
					
					
					<td>
						2
					</td>
					<td>
						2.0
					</td>
					<td>
						<input type="hidden" name="outputNum" class="outputNumIh" value="2"/>
						2
					</td>
					<td>
						<input type="hidden" name="outputWeight" class="outputWeightIh" value="2.0"/>
						2.0
					</td>
					<td><input type="text" name="realNum" class="realNumIp digit required" style="width:45px;" onchange="checkRealNum(this);calcuTotal();" onkeydown="clearNoNum2(this)" value="2" maxlength="9"/><label class="relNumUnitName">件</label></td>
					<td><input type="text" name="realWeight" class="realWeightIp required" style="width:65px;" onchange="formatDecimal(this);calcuTotal();checkRealWeight(this);" onkeydown="clearNoNum(this);" value="2.000" maxlength="11"/><label class="relWeightUnitName'''
    str2 = "hhhh"
    filename = "C:\\Users\\中拓电商tcy\\PycharmProjects\\testProject\\temp_html\\CKST-002.html"
    op = OperationHtml(filename)
    print(op.GetValue("name", "driverId"))
