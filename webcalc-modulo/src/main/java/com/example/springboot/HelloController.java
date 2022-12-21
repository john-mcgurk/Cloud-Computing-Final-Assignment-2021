package com.example.springboot;

import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MissingServletRequestParameterException;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.method.annotation.MethodArgumentTypeMismatchException;

import java.util.HashMap;


@RestController
public class HelloController {

	@RequestMapping(path="/")
	public ResponseEntity<HashMap<String, String>> modulo(@RequestParam String x, @RequestParam String y) throws MissingServletRequestParameterException {
		String ans = "";
		System.out.println("Im in here with type string " + x);
		int X,Y;
		try {
			X = Integer.parseInt(x);
			Y = Integer.parseInt(y);
		} catch (NumberFormatException e) {
			throw new MissingServletRequestParameterException("x", "y") ;
		}

		HashMap<String, String> res = new HashMap<>();
		HttpHeaders headers = new HttpHeaders();
		headers.setAccessControlAllowOrigin("*");
		headers.setContentType(MediaType.APPLICATION_JSON);
		if (Y == 0) {
			res.put("answer", "undefined");
			res.put("string", X + "%"+Y+"= Undefined");
			res.put("error", "true");
		}
		else {
			ans = Integer.toString((X%Y));
			res.put("answer", ans);
			res.put("string", X + "%" + Y + "=" + ans);
			res.put("error", "false");
		}

		return new ResponseEntity<>(
				res, headers, 200);
	}

	@ExceptionHandler({MissingServletRequestParameterException.class, MethodArgumentTypeMismatchException.class})
	public ResponseEntity<HashMap<String, String>> handleMissingParams(MissingServletRequestParameterException ex) {
		HashMap<String, String> res = new HashMap<>();
		HttpHeaders headers = new HttpHeaders();
		headers.setAccessControlAllowOrigin("*");
		headers.setContentType(MediaType.APPLICATION_JSON);
		res.put("answer", "undefined");
		res.put("string", "Error - Missing parameters");
		res.put("error", "True");

		return new ResponseEntity<>(
				res, headers, 200);
		// Actual exception handling
	}

}
