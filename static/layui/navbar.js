layui.use(['element','layer','laytpl'], function(){
    var element = layui.element; //导航的hover效果、二级菜单等功能，需要依赖element模块
    var laytpl = layui.laytpl;

    var data = { //数据
        "title":"Layui常用模块"
        ,"list":[{"modname":"弹层","alias":"layer","site":"layer.layui.com"},{"modname":"表单","alias":"form"}]
    };

    var ht =
      "<h3>{{ d.title }} </h3><ul>"+
       " {{#  layui.each(d.list, function(index, item){ }}"+
        "<li>"+
          "<span>{{ item.modname }} </span>"+
          "<span>{{ item.alias }}：</span>"+
          "<span>{{ item.site || '' }}</span>"+
        "</li>"+
        "{{#  }); }}"+
        "{{#  if(d.list.length === 0){ }}"+ "无数据" +
            "{{#  } }}"+
      "</ul>"
    var getTpl = ht
        // console.log(getTpl)
    ,view = document.getElementById('view');
        // console.log(view);
    laytpl(getTpl).render(data, function(html){
        view.innerHTML = html;
    });




    //监听导航点击
    element.on('nav(leftbar)', function(elem){
        console.log(elem);
        //layer.msg(elem.text());
        if (elem.text() == "系数明细"){
            //layui.jquery("#allbody").empty();

            layui.jquery("#allbody").html(
        '<div style="padding: 15px;">内容主体区域</div>'+
                '<div class="layui-btn-group demoTable">'+
                '<button class="layui-btn" data-type="getCheckData" lay-event="mutidel">删除选中行数据</button>'+
                '<button class="layui-btn" data-type="getCheckLength">获取选中数目</button>'+
                '<button class="layui-btn" data-type="isAll">验证是否全选</button>'+
                '</div>'+
                '<table class="layui-hide" id="idTest" lay-filter="demo"></table>'+
                '<script type="text/html" id="barDemo">'+
                '<a class="layui-btn layui-btn-primary layui-btn-sm" lay-event="detail">查看</a>'+
                '<a class="layui-btn layui-btn-sm" lay-event="update">更新</a>'+
                '<a class="layui-btn layui-btn-danger layui-btn-sm" lay-event="del">删除</a>'+
                '</script>'+
                '<script src="/static/layui/tablerender.js"></script>'
                
        );

        }
        if (elem.text() == "数据上传"){

            layui.jquery("#allbody").empty();

            layui.jquery("#allbody").html(
                '<script src="/static/layui/uploadfile.js"></script>'+
                '<div class="layui-upload">'+
                '<button type="button" class="layui-btn layui-btn-normal" id="testList">选择多文件</button>'+
                '<div class="layui-upload-list">'+
                '<table class="layui-table">'+
                '<thead>'+
                '<tr><th>文件名</th>'+
                '<th>大小</th>'+
                '<th>状态</th>'+
                '<th>操作</th>'+
                '</tr></thead>'+
                '<tbody id="demoList"></tbody>'+
                '</table>'+
                '</div>'+
                '<button type="button" class="layui-btn" id="testListAction">开始上传</button>'+
                '</div>'

            );

        }
    });
});

