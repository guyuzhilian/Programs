package com.lidajun.listviewtest;

import java.util.ArrayList;
import java.util.List;

import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;
import android.view.View;


public class MainActivity extends ActionBarActivity {
	
	private List<Fruit> fruitList = new ArrayList<Fruit>();
	
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initFruits();
        FruitAdapter adapter = new FruitAdapter(MainActivity.this, R.layout.fruit_item, fruitList);
        ListView listView = (ListView) findViewById(R.id.list_view);
        listView.setAdapter(adapter);
        
        listView.setOnItemClickListener(new OnItemClickListener() {
        	@Override
        	public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        		Fruit fruit = fruitList.get(position);
        		Toast.makeText(MainActivity.this, fruit.getName(), Toast.LENGTH_SHORT).show();
        	}
        });
    }
    
    private void initFruits() {
    	Fruit apple = new Fruit("Apple", R.drawable.apple_pic);
    	fruitList.add(apple);
    	Fruit banana = new Fruit("Banana", R.drawable.banana_pic);
    	fruitList.add(banana);
    	Fruit orange = new Fruit("Orange", R.drawable.orange_pic);
    	fruitList.add(orange);
    	Fruit watermelon = new Fruit("Watermelon", R.drawable.watermelon_pic);
    	fruitList.add(watermelon);
    	Fruit pear = new Fruit("Pear", R.drawable.pear_pic);
    	fruitList.add(pear);
    	Fruit grape = new Fruit("Grape", R.drawable.grape_pic);
    	fruitList.add(grape);
    	Fruit pineapple = new Fruit("Pineapple", R.drawable.pineapple_pic);
    	fruitList.add(pineapple);
    	Fruit strawberry = new Fruit("Strawberry", R.drawable.strawberry_pic);
    	fruitList.add(strawberry);
    	Fruit cherry = new Fruit("Cherry", R.drawable.cherry_pic);
    	fruitList.add(cherry);
    	Fruit mango = new Fruit("Mango", R.drawable.mango_pic);
    	fruitList.add(mango);
    	}

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
}
