
//function getFormData($form){
//    var unindexed_array = $form.serializeArray();
//    var indexed_array = {};
//
//    $.map(unindexed_array, function(n, i){
//        indexed_array[n['name']] = n['value'];
//    });
//    alert(indexed_array)
//    return indexed_array;
//}
//$(document).ready(function() {
//$('#submit').on('click', function(e) {
//    $.getJSON("/", function(data){
//        console.log(data)
//
//    });
//  });
//  });


//$(document).ready(function() {
//   $("#submit").click(function() {
//       $("#form_data").submit();
//   });
//});

// $(document).ready(function() {
//
//          $('#submit').on('click', function(e) {
//            e.preventDefault()
////         var $form = $("#form_data");
////        var data = getFormData($form);
//        $.getJSON('/', function(datas) {
//            var data= datas
//        console.log(datas);
////
//     $.ajax({
//      type: 'POST',
//      url: "postDB",
//      data:JSON.stringify(data),
//      dataType: "JSON",
//      contentType: "application/json; charset=utf-8",
//      traditional: true,
//      success: function(resultData) {
//        alert("Save Complete")
//    }
//        });
//         });
// });
// });

//function getjsonData(){
//var data =$('#response').text(JSON.stringify(response));
////var datas =$('#response').text(data.output).show();
// $.ajax({
//  type: 'POST',
//  url: "postDB",
//  data:JSON.stringify(data),
//  dataType: "JSON",
//  contentType: "application/json; charset=utf-8",
//  traditional: true,
//  success: function(resultData) {
//    alert("Save Complete")
//}
//    });
// }
// $(document).ready(function() {
//
//  $('#submit').on('click', function(e) {
//    e.preventDefault()
//    getjsonData()
//
//             });
// });