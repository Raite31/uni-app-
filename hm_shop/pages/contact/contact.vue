<template>
	<view class="contact">
		<image class="img" src="http://www.itcast.cn/2018czydz/images/gywmban.jpg"></image>
		<view class="info">
			<view @click="callPhone">联系电话：13433094759（点击拨打）</view>
			<view>校区地址：你心里</view>
		</view>
		<map class="map" :longitude="longitude" :scale="scale" :latitude="latitude" :markers="markers"></map>
	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				longitude: 112.867739,
				latitude: 22.498471,
				scale: 15,
				markers:[
					{
						longitude: 112.867739,
						latitude: 22.498471,
						iconPath: '../../static/hmlogo.png',
						width: 30,
						height: 30
					}
				]
			}
		},
		methods: {
			callPhone(){
				uni.makePhoneCall({
					phoneNumber: '13433094759'
				})
			}
		}
	}
</script>

<style lang="scss">
	.contact{
		.img{
			width: 750rpx;
			height: 320rpx;
		}
	}
	.info{
		padding: 10rpx 20rpx;
		font-size: 30rpx;
		view{
			line-height: 80rpx;
			border-bottom: 1px solid #eee;
		}
	}
	.map{
		width: 750rpx;
		height: 750rpx;
	}
</style>
