<template>
  <div>
    <div v-if="dog.detail" class="dog-info">
        <p><strong>이름: </strong>{{ dog.detail.name }}</p>
        <p><strong>품종: </strong>{{ dog.detail.breed_group }}</p>
        <p><strong>높이:</strong> {{ dog.detail.height.imperial }} 인치 ({{ dog.detail.height.metric }} cm)</p>
        <p><strong>수명:</strong> {{ dog.detail.life_span }}</p>
        <p><strong>성격:</strong> {{ dog.detail.temperament }}</p>
        <p><strong>무게:</strong> {{ dog.detail.weight.imperial }} 파운드 ({{ dog.detail.weight.metric }} kg)</p>
      </div>
    <div v-else class="dog-info">
      상세 정보 없음
    </div>
  </div>
</template>

<script setup>

const props = defineProps({
  dog: Object
})

</script>

<style scoped>
.dog-info {
  margin-left: 10px;
}

</style>