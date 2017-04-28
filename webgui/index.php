<!DOCTYPE html>
<html>
<head>
    <title>IoT security scanner</title>
    <!-- for-mobile-apps -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <!-- //for-mobile-apps -->
    <link href="css/bootstrap.css" rel="stylesheet" type="text/css" media="all" />
    <link href="css/style.css" rel="stylesheet" type="text/css" media="all" />
    <!-- js -->
    <script src="js/jquery-1.11.1.min.js"></script>
    <!-- //js -->
    <link href='https://fonts.googleapis.com/css?family=UnifrakturMaguntia' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:600,600italic,700,400' rel='stylesheet' type='text/css'>
    <!-- FlexSlider -->
    <link rel="stylesheet" href="css/flexslider.css" type="text/css" media="screen" />
    <?php
    if(isset($_GET['success'])) {
        ?>
        <script>alert("Успешно! Ожидайте письмо с результатами");</script>
        <?
    }else if(isset($_GET['failure'])) {
        ?>
        <script>alert("Что-то пошло не так. Повторите запрос");</script>
        <?
    }
    ?>
    <script defer src="js/jquery.flexslider.js"></script>
    <script type="text/javascript">
        $(window).load(function(){
            $('.flexslider').flexslider({
                animation: "slide",
                start: function(slider){
                    $('body').removeClass('loading');
                }
            });
        });
    </script>
    <!-- //FlexSlider -->
    <link href='//fonts.googleapis.com/css?family=Open+Sans:400,300,300italic,400italic,600,600italic,700,700italic,800,800italic' rel='stylesheet' type='text/css'>
</head>

<body>
<!-- banner -->
<div class="banner">
    <div class="container">
        <div class="banner-info">
            <div class="col-md-6 banner-info-left">
            </div>
            <div class="col-md-6 banner-info-right">
                <div class="sap_tabs">
                    <div id="horizontalTab" style="display: block; width: 100%; margin: 0px;">
                        <ul class="resp-tabs-list">
                            <li class="resp-tab-item grid1" aria-controls="tab_item-0" role="tab"><span>IoT security checker</span></li>
                            <div class="clear"></div>
                        </ul>
                        <div class="resp-tabs-container">
                            <div class="tab-1 resp-tab-content" aria-labelledby="tab_item-0">
                                <div class="facts">
                                    <div class="sign-in-form">
                                        <div class="in-form">
                                            <form action="proc.php" method="post">
                                                <input type="text" placeholder="Hostname of device" required=" " name="hostname">
                                                </br>
                                                </br>
                                                <input type="text" placeholder="Your email for report" required=" " name="email">
                                                <div class="ckeck-bg">
                                                    <div class="checkbox-form">
                                                        <div class="check-left">
                                                        </br>
                                                            <div class="check">
                                                                <label class="check"><input type="checkbox" name="adv" ><i> </i>Advanced check</label>
                                                            </div>
                                                        </div>
                                                        <div class="check-right">
                                                            <input type="submit" value="Submit">
                                            </form>
                                        </div>
                                        <div class="clearfix"> </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="js/easyResponsiveTabs.js" type="text/javascript"></script>
    <script type="text/javascript">
        $(document).ready(function () {
            $('#horizontalTab').easyResponsiveTabs({
                type: 'default', //Types: default, vertical, accordion
                width: 'auto', //auto or any width like 600px
                fit: true   // 100% fit in a container
            });
        });
    </script>
</div>
<div class="clearfix"> </div>
</div>
</div>
</div>
<script src="js/bootstrap.js"> </script>
<!-- //for bootstrap working -->
</body>
</html>