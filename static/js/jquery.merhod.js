                $(document).ready(function() {
                    //##### send add record Ajax request to response.php #########
                    $("#FormSubmit").click(function (e) {
                            e.preventDefault();
                            if($("#contentText").val()==='')
                            {
                                alert("Введите текст!");
                                return false;
                            }
                            var myData = 'content_txt='+ $("#contentText").val(); //build a post data structure
                            jQuery.ajax({
                            type: "POST", // HTTP method POST or GET
                            url: "response.php", //Where to make Ajax calls
                            dataType:"text", // Data type, HTML, json etc.
                            data:myData, //Form variables
                            success:function(response){
                                $("#responds").append(response);
                                $("#contentText").val(''); //empty text field on successful
                            },
                            error:function (xhr, ajaxOptions, thrownError){
                                alert(thrownError);
                            }
                            });
                    });

                    //##### Send delete Ajax request to response.php #########
                    $("body").on("click", "#responds .del_session", function(e) {
                         e.returnValue = false;
                         var clickedID = this.id.split('-'); //Split string (Split works as PHP explode)
                         var DbNumberID = clickedID[1]; //and get number from array
                         var myData = 'recordToDelete='+ DbNumberID; //build a post data structure

                            jQuery.ajax({
                            type: "POST", // HTTP method POST or GET
                            url: "response.php", //Where to make Ajax calls
                            dataType:"text", // Data type, HTML, json etc.
                            data:myData, //Form variables
                            success:function(response){
                                //on success, hide  element user wants to delete.
                                $('#item_'+DbNumberID).fadeOut("slow");
                            },
                            error:function (xhr, ajaxOptions, thrownError){
                                //On error, we alert user
                                alert(thrownError);
                            }
                            });
                    });
                    //##### Send delete Ajax request to response.php #########
                    $("body").on("click", "#respondsuser .del_user", function(e) {
                         e.returnValue = false;
                         var clickedID = this.id.split('-'); //Split string (Split works as PHP explode)
                         var DbNumberID = clickedID[1]; //and get number from array
                         var myData = 'recordToDeleteUser='+ DbNumberID; //build a post data structure

                            jQuery.ajax({
                            type: "POST", // HTTP method POST or GET
                            url: "response.php", //Where to make Ajax calls
                            dataType:"text", // Data type, HTML, json etc.
                            data:myData, //Form variables
                            success:function(response){
                                //on success, hide  element user wants to delete.
                                $('#itemuser_'+DbNumberID).fadeOut("slow");
                            },
                            error:function (xhr, ajaxOptions, thrownError){
                                //On error, we alert user
                                alert(thrownError);
                            }
                            });
                    });
                    // для первых трех
                    $("body").on("click", "#responds .del_button2", function(e) {
                                $(this).parent('div').parent('li').fadeOut("slow");
                    });


                });