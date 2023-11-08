<template>
  <div class="header">
    <h2>랜덤한 강아지</h2>
    <button @click="getRandomDogData" class="button">새로운 강아지 가져오기</button>
  </div>
  <div v-if="dogIsEmpty" class="dog-container">
    <div v-for="dog in dogs" class="dog-box">
      <img :src="dog.url" alt="">
      <DogDetail :dog="dog"/>
      <!-- <div v-if="dog.detail" class="dog-info">
        <p><strong>이름: </strong>{{ dog.detail.name }}</p>
        <p><strong>품종: </strong>{{ dog.detail.breed_group }}</p>
        <p><strong>높이:</strong> {{ dog.detail.height.imperial }} 인치 ({{ dog.detail.height.metric }} cm)</p>
        <p><strong>수명:</strong> {{ dog.detail.life_span }}</p>
        <p><strong>성격:</strong> {{ dog.detail.temperament }}</p>
        <p><strong>무게:</strong> {{ dog.detail.weight.imperial }} 파운드 ({{ dog.detail.weight.metric }} kg)</p>
      </div>
      <div v-else class="dog-info">
        상세 정보 없음
      </div> -->
    </div>
  </div>
  <div v-else>
    아직 데이터를 받아오지 않았다.
  </div>
</template>

<script setup>
import {computed, watch} from 'vue';
import DogDetail from '@/components/DogDetail.vue'
const emit = defineEmits(['getDogData'])

const getRandomDogData = () => {
  emit('getDogData')
}

const props = defineProps({
  dogs: Array
})

watch(props, () => {
  console.log(props.dogs)
})


const dogIsEmpty = computed(() => {
  // script에서는 props.<변수>로 접근해야 한다.
  return props.dogs.length > 0 ? true : false
})

</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}
.button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #3498db;
  color: #fff;
  font-size: 16px;
  text-align: center;
  text-decoration: none;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

/* 버튼 호버 효과 */
.button:hover {
  background-color: #51a7e8;
}

/* 버튼 클릭 효과 */
.button:active {
  background-color: #1f78b4;
}

.dog-container {
  border: 1px solid #000;
}

.dog-box {
  display: flex;
  border: 1px solid #000;
  margin: 10px;
  border-radius: 10px;
}

.dog-box img {
  width: 200px;
  height: 200px;
  object-fit: fill;
  border-radius: 10px;
}


</style>