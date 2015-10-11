$(function() {
	//新增月份.其他花費btn處理
	$('#otheroutcome_newbtn').click(function() {
		var txt1 = "<p><input type='checkbox' name='other_chk[]' /> <input type='text' name='other_cost_name' style='width:100px;' placeholder='名稱'/> <input type='number' name='other_cost' style='width:100px;' placeholder='金額'/><select id='nmonthcash_type_cost[]' name='nmonthcash_type_cost' style='width:100px;'>"+$("#outcome_type1").html()+"</select></p>";
		$("#other_cost").append(txt1);
	});
	$('#otheroutcome_delbtn').click(function() {
		$("#other_cost input[type=checkbox]:checked").each(function() {
			$(this).parent().remove();
		});
	});
	//新增月份.短期固定成本btn處理
	$('#otherincome_newbtn').click(function() {
		var txt1 = "<p><input type='checkbox' name='short_chk[]' /> <input type='text' name='other_income_name' style='width:100px;' placeholder='名稱'/> <input type='number' name='other_income' style='width:100px;' placeholder='金額'/></p>";
		$("#other_income").append(txt1);
	});
	$('#otherincome_delbtn').click(function() {
		$("#other_income input[type=checkbox]:checked").each(function() {
			$(this).parent().remove();
		});
	});
});