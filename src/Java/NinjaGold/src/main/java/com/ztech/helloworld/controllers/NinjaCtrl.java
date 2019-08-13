package com.ztech.helloworld.controllers;

import javax.servlet.http.HttpSession;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.concurrent.ThreadLocalRandom;
import java.util.ArrayList;
import java.util.Date;

@Controller
public class NinjaCtrl {
	ArrayList<ArrayList> updates = new ArrayList<ArrayList>();
	int gold = 0;
	Date dateTime = new java.util.Date();
	String time = String.format("(%s %te %<tB %<tY %<tI:%<tM %<tp)", "", dateTime);

	@RequestMapping("/")
	public String index(HttpSession session) {
		session.setAttribute("gold", gold);
		return "index.jsp";
	}

	@PostMapping("/process_money")
	public String money(@RequestParam(value="building") String building, HttpSession session) {


		switch(building) {
		case "farm":
			int amt = ThreadLocalRandom.current().nextInt(10, 21);
			gold += amt;
			String color = "green";
			String msg = "You earned " + amt + " from the " + building + "!";
			ArrayList<String> data = new ArrayList<String>();
			data.add(color);
			data.add(msg);
			data.add(time);
			updates.add(0, data);
			break;
			
		case "cave":
			amt = ThreadLocalRandom.current().nextInt(5, 11);
			gold += amt;
			color = "green";
			msg = "You earned " + amt + " from the " + building + "!";
			data = new ArrayList<String>();
			data.add(color);
			data.add(msg);
			data.add(time);
			updates.add(0, data);
			break;
			
		case "house":
			amt = ThreadLocalRandom.current().nextInt(2, 6);
			gold += amt;
			color = "green";
			msg = "You got " + amt + " from the " + building + "!";
			data = new ArrayList<String>();
			data.add(color);
			data.add(msg);
			data.add(time);
			updates.add(0, data);
			break;
			
		case "casino":
			amt = ThreadLocalRandom.current().nextInt(-50, 51);
			gold += amt;
			if (amt < 0) {
				color = "red";
				msg = "You lost " + amt + " at the " + building + "!";
			}
			else if (amt == 0){
				color = "red";
				msg = "No gain!";
			}
			else {
				color = "green";
				msg = "You won " + amt + " at the " + building + "!";
			}
			data = new ArrayList<String>();
			data.add(color);
			data.add(msg);
			data.add(time);
			updates.add(0, data);
			break;
		}


		session.setAttribute("updates", updates);
		session.setAttribute("size", updates.size() - 1);
		return "redirect:/";
	}
}