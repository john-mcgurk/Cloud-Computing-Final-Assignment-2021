using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using Microsoft.AspNetCore.Mvc.ModelBinding;

// For more information on enabling MVC for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace webcalc_square.Controllers
{
    public class Result
    {
        public string answer;
        public string query;
        public string error;
    }

    [Route("/welcome")]
    public class WelcomeController : Controller
    {
        [HttpGet]
        public IActionResult welcome()
        {
            string resp = "Landing Screen for Square operation webcalc :)";
            return Content(resp);
        }
    }


    [Route("/")]
    public class HomeController : Controller
    {
        private string response;

        [HttpGet]
        public IActionResult squareNum([FromQuery] String x, [FromQuery] String y)
        {
            int X, Y;
            if (int.TryParse(x, out X) && int.TryParse(y, out Y)) {
              int ans = Convert.ToInt32(Math.Pow(X,Y));
              response = JsonConvert.SerializeObject(
                  new Result
                  {
                      answer = ans.ToString(),
                      error = "false",
                      query = x + "^" + y + "=" + ans
                  });
            }
            else {
                response = JsonConvert.SerializeObject(
                  new Result {
                    answer = "undefined",
                    error = "true",
                    query = "error - invalid parameters"
                  });
            }


            return Content(response, "application/json");

        }
    }
}
