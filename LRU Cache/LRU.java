import java.util.LinkedHashMap;
import java.util.Map;

class LRUCache{
    private Map<Integer, Integer> map;
    private int capacity;
    public LRUCache(int capacity){
        this.capacity = capacity;
        map = new LinkedHashMap<Integer, Integer>(capacity+1);
    }
    public int get(int key){
        Integer val = map.get(key);
        if (val == null) return -1;
        map.remove(key);
        map.put(key, val); 
        return val;
    }
    public void put(int key, int value){
        map.remove(key);
        map.put(key, value);
        if (map.size() > capacity){
            map.remove(map.entrySet().iterator().next().getKey());
        }
    }
}

