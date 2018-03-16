layui.use('table', function(){
    var table = layui.table;
    table.render({
        elem: '#idTest'
        ,url:'/goods/'
        ,height: 'full-200'
        ,page: { //支持传入 laypage 组件的所有参数（某些参数除外，如：jump/elem） - 详见文档
            layout: ['limit', 'count', 'prev', 'page', 'next', 'skip'] //自定义分页布局
            //,curr: 5 //设定初始在第 5 页
            ,groups: 3 //只显示 1 个连续页码
            ,first: false //不显示首页
            ,last: false//不显示尾页

        }

        ,cellMinWidth: 80 //全局定义常规单元格的最小宽度，layui 2.2.1 新增
        ,cols: [[
            {type:'checkbox', fixed: 'left'}
            //,{field:'id',  wide:80, sort: true, title:"id"}
            ,{field:'st_idcardnum',edit:true, title:"员工身份证号"}
            ,{field:'st_name',edit:true, title:"姓名"}
            ,{field:'st_depart',edit:true,sort: true,title:"部门"}
            ,{field:'st_joindyears', edit:true,sort: true,title:"参加工作时间"}
            ,{field:'st_yearsofworking', edit:true,sort: true,title:"工作年限"}
            ,{field:'st_demandyears', edit:true,sort: true,title:"要求工作年限"}
            ,{field:'st_scoreofyears', edit:true,sort: true,title:"年限得分"}
            ,{field:'st_education', edit:true,sort: true,title:"学历"}
            ,{field:'st_demandeducation', edit:true,sort: true,title:"学历要求"}
            ,{field:'st_educationscore', edit:true,sort: true,title:"学历得分"}
            ,{field:'st_title',edit:true,sort: true,title:"职称"}
            ,{field:'st_demandtitle', edit:true,sort: true,title:"职称要求"}
            ,{field:'st_scoreoftitle', edit:true,sort: true,title:"职称得分"}
            ,{field:'st_scoreofprimaryccbp', edit:true,sort: true,title:"初级银行从业得分"}
            ,{field:'st_scoreofmiddleCCBP', edit:true,sort: true,title:"中级银行从业得分"}
            ,{field:'st_internaltrainer', edit:true,sort: true,title:"内训师"}
            ,{field:'st_scoreofinternaltrainer', edit:true,sort: true,title:"内训师得分"}
            ,{field:'st_scoreofallcertificates', edit:true,sort: true,title:"所有证书得分"}
            ,{field:'st_rankeofinternal', edit:true,sort: true,title:"内部级数"}
            ,{field:'st_coefficient',edit:true,sort: true,title:"工资系数"}
            ,{field:'right', width:177 ,toolbar: '#barDemo'}

        ]]
    });

    // Idcardnum              string        `gorm:"not null;unique" form:"st_idcardnum" json:"st_idcardnum"`                    //员工身份证号
    // Name                   string        `gorm:"not null" form:"st_name" json:"st_name"`                                     //姓名
    // Departement            string        `gorm:"varchar(100)" form:"st_depart" json:"st_depart"`                             //部门
    // Rank                   int           `gorm:"not null" form:"st_rank" json:"st_rank"`                                     //员工等级
    // JoindYears             string        `gorm:"not null" form:"st_joindyears" json:"st_joindyears"`                         //参加工作时间
    // YearsOfWroking         int           `gorm:"not null" form:"st_yearsofworking" json:"st_yearsofworking"`                 //工作年限
    // DemandYears            int           `gorm:"not null" form:"st_demandyears" json:"st_demandyears"`                       //要求工作年限
    // ScoreOfYears           int           `gorm:"not null" form:"st_scoreofyears" json:"st_scoreofyears"`                     //年限得分
    // Eductaion              string        `gorm:"not null" form:"st_education" json:"st_education"`                           //学历
    // DemandEducation        string        `gorm:"not null" form:"st_demandeducation" json:"st_demandeducation"`               //学历要求
    // EducationScore         int           `gorm:"not null" form:"st_educationscore" json:"st_educationscore"`                 //学历得分
    // Title                  string        `gorm:"type:varchar(100)" form:"st_title" json:"st_title"`                          //职称
    // DemandTitle            string        `gorm:"type:varchar(100)" form:"st_demandtitle" json:"st_demandtitle"`              //职称要求
    // ScoreOfTitle           int           `gorm:"not null" form:"st_scoreoftitle" json:"st_scoreoftitle"`                      //职称得分
    // PrimaryCCBP            int           `gorm:"not null" form:"st_primaryCCBP" json:"st_primaryCCBP"`                       //初级银行从业
    // DemandPrimaryCCBP      int           `gorm:"not null" form:"st_demandprimaryCCBP" json:"st_demandprimaryCCBP"`           //初级银行从业要求
    // ScoreOfPrimaryCCBP     int           `gorm:"not null" form:"st_scoreofprimaryccbp" json:"st_scoreofprimaryccbp"`         //初级银行从业得分
    // MiddleCCBP             int           `gorm:"not null" form:"st_middleCCBP" json:"st_middleCCBP"`                         //中级银行从业
    // ScoreOfMiddleCCBP      int           `gorm:"not null" form:"st_scoreofmiddleCCBP" json:"st_scoreofmiddleCCBP"`           //中级银行从业得分
    // InternalTrainer        string        `gorm:"type:varchar(100)" form:"st_internaltrainer" json:"st_internaltrainer"`      //内训师
    // ScoreOfInternalTrainer int           `gorm:"not null" form:"st_scoreofinternaltrainer" json:"st_scoreofinternaltrainer"` //内训师得分
    // Certificates           []Certificate `gorm:"not null" form:"certificates" json:"certificates"`
    // ScoreOfAllCertificates int           `gorm:"not null" form:"st_scoreofallcertificates" json:"st_scoreofallcertificates"` //所有证书得分
    // FinalScore             int           `gorm:"not null" form:"st_finalscore" json:"st_finalscore"`                        //总得分
    // RankOfInternal         int           `gorm:"not null" form:"st_rankeofinternal" json:"st_rankeofinternal"`              //内部级数
    // Coefficient            float32       `gorm:"not null" form:"st_coefficient" json:"st_coefficient"`                      //工资系数

    //监听表格复选框选择
    table.on('checkbox(demo)', function(obj) {
        console.log(obj)
    });
    table.on('edit(demo)', function(obj){

              var value = obj.value //得到修改后的
            ,data = obj.data //得到所在行所有键值
            ,field = obj.field;//得到字段

         if(field == 'st_yearsofworking'){
             obj.data.st_yearsofworking= parseInt(value)
         }else if (field == 'st_rank'){
             obj.data.st_rank= parseInt(value)
         }else if (field == 'st_demandyears') {
             obj.data.st_demandyears = parseInt(value)
         }else if (field == 'st_scoreofyears'){
             obj.data.st_scoreofyears= parseInt(value)
         }else if (field == 'st_educationscore') {
             obj.data.st_educationscore = parseInt(value)
         }else if (field == 'st_scoreoftitle'){
             obj.data.st_scoreoftitle= parseInt(value)
         }else if (field == 'st_primaryCCBP') {
             obj.data.st_primaryCCBP = parseInt(value)
         }else if (field == 'st_demandprimaryCCBP'){
             obj.data.st_demandprimaryCCBP= parseInt(value)
         }else if (field == 'st_scoreofprimaryccbp') {
             obj.data.st_scoreofprimaryccbp = parseInt(value)
         }else if (field == 'st_middleCCBP') {
             obj.data.st_middleCCBP = parseInt(value)
         }else if (field == 'st_scoreofmiddleCCBP'){
             obj.data.st_scoreofmiddleCCBP= parseInt(value)
         }else if (field == 'st_scoreofinternaltrainer') {
             obj.data.st_scoreofinternaltrainer = parseInt(value)
         }else if (field == 'st_scoreofallcertificates'){
             obj.data.st_scoreofallcertificates= parseInt(value)
         }else if (field == 'st_finalscore') {
             obj.data.st_finalscore = parseInt(value)
         }else if (field == 'st_rankeofinternal'){
             obj.data.st_rankeofinternal= parseInt(value)
         }else if (field == 'st_coefficient') {
             obj.data.st_coefficient = parseFloat(value)
         }
        layer.msg('[ID: '+ data.ID +'] ' + field + '字段更改为:'+ value);

    });
    //监听工具条
    table.on('tool(demo)', function(obj){
        var data = obj.data;
        var msg = ""
        var html = '<div class="layui-form">'+
            '<table class="layui-table" id="certable">'+
            '<colgroup> <col width="150"> <col width="150"> <col width="200"> <col> </colgroup>'+
            '<thead> <tr> <th>证书名称</th> <th>证书得分</th> <th>添加时间</th></tr> </thead><tbody>'



        if(obj.event === 'detail'){
            if(data.certificates.length != 0){
                for (i = 0; i<data.certificates.length; i++){
                    html = html+"<tr> <td>"+data.certificates[i].certificate+
                        "</td> <td>"+data.certificates[i].scoreofcertificate+
                        "</td> <td>"+data.certificates[i].CreatedAt+"</td></tr>"
                   // msg = msg + data.certificates[i].certificate
                }
            }else{
                html = html +"<tr> <td>证书信息不存在</td></tr>>"
            }
            //layer.msg('ID：'+ data.ID + ' 的查看操作'+data.certificates[0].certificate);


            layer.open({
                type: 1,
                title: '账户信息详情',
                shadeClose: true,
                shade: false,
                maxmin: true, //开启最大化最小化按钮
                area: ['800px', '300px'],
                content: html+'</tbody> </table> </div>'
            });
        } else if(obj.event === 'del'){
            layer.confirm('真的删除行么', function(index){

                layui.jquery.ajax(
                    {
                        url: '/api/v1/delstaffrecord',
                        type: 'DELETE',
                        contentType: 'application/json;charset=utf-8',

                        data: JSON.stringify(data),
                        error : function (res) {
                            layer.alert(res);
                        },
                        success : function (res) {

                            obj.del();
                            layer.close(index);
                        }
                    }
                );

            });
        } else if(obj.event === 'update'){
           // console.log(obj.data)
            layui.jquery.ajax(
                {
                    url: '/api/v1/updatestaffrecord',
                    type: 'PUT',
                    contentType: 'application/json;charset=utf-8',

                    data: JSON.stringify(data),
                    error : function (res) {
                        layer.alert(res);
                    },
                    success : function () {
                        layer.alert('更新行：<br>'+
                            '姓名:'+data.st_name+'<br>')
                        //obj.del();
                        // layer.close(index);
                    }

                }
            );

        }
    });

    var $ = layui.$, active = {
        getCheckData: function(obj,index){ //获取选中数据
            var checkStatus = table.checkStatus('idTest')
                ,data = checkStatus.data;
            layer.confirm('真的删除行么', function(index) {
                //  layer.alert(JSON.stringify(data));
                for (i = 0; i < data.length; i++) {
                    layui.jquery.ajax(
                        {
                            url: '/api/v1/delstaffrecord',
                            type: 'DELETE',
                            contentType: 'application/json;charset=utf-8',
                            data: JSON.stringify(data[i]),
                            error: function (res) {
                                layer.alert(res);
                            },
                            success: function (res) {
                                //checkStatus.index
                                console.log(res)

                            }
                        }
                    );
                }
                layer.close(index);
                table.reload('idTest');
            });

        }
        ,getCheckLength: function(){ //获取选中数目
            var checkStatus = table.checkStatus('idTest')
                ,data = checkStatus.data;
            layer.msg('选中了：'+ data.length + ' 个');
        }
        ,isAll: function(){ //验证是否全选
            var checkStatus = table.checkStatus('idTest');
            layer.msg(checkStatus.isAll ? '全选': '未全选')
        }
    };

    $('.demoTable .layui-btn').on('click', function(){
        var type = $(this).data('type');
        active[type] ? active[type].call(this) : '';
    });
    $('.demoTable .layui-btn').on('click', function(){
        var type = $(this).data('type');
        active[type] ? active[type].call(this) : '';
    });
});
